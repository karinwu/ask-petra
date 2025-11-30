import json
import os
import requests
import boto3
import numpy as np
from sentence_transformers import SentenceTransformer
from huggingface_hub import configure_http_backend

model_name = 'multi-qa-MiniLM-L6-cos-v1'
model = SentenceTransformer(model_name)

# Get the directory of the current file for relative path
current_dir = os.path.dirname(os.path.abspath(__file__))
faq_path = os.path.join(current_dir, "data", "faq.json")

with open(faq_path, "r") as f:
    faq = json.load(f)

faq_items = []
for section in faq:
    for item in section["data"]:
        faq_items.append({
            "question": item["question"],
            "answer": item["text"],
            "type": section["type"]
        })

faq_questions = [item["question"] for item in faq_items]
faq_embeddings = model.encode(faq_questions, normalize_embeddings=True)


def vector_search(
        user_question,
        top_k=1,
        threshold=0.75
):
    user_emb = model.encode([user_question], normalize_embeddings=True)
    scores = np.dot(faq_embeddings, user_emb.T).flatten()
    best_idx = np.argmax(scores)
    if scores[best_idx] >= threshold:
        return faq_items[best_idx]
    else:
        return None


def call_claude3(
        prompt_text,
        temperature=0.3
):
    bedrock_runtime = boto3.client(
        service_name='bedrock-runtime',
        region_name='us-east-1'
    )
    model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

    # Add system prompt for consistent Petra personality
    system_prompt = """You are Petra, a helpful chatbot for the risk modeling team.
    Keep responses professional but friendly. If you don't know something
    specific about risk modeling, say so rather than guessing.
    End responses with 'Meow' to maintain your cat personality."""

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 500,
        "temperature": temperature,
        "system": system_prompt,
        "messages": [
            {"role": "user", "content": prompt_text}
        ],
    })
    response = bedrock_runtime.invoke_model(
        body=body,
        modelId=model_id,
        contentType="application/json",
        accept="application/json"
    )
    response_body = json.loads(response['body'].read())
    return response_body['content'][0]['text']


def chatbot_rag(user_question):
    faq_result = vector_search(user_question)
    if faq_result is not None:
        return faq_result["answer"]
    else:
        return call_claude3(user_question)
