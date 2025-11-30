# Ask Petra 🐱

![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Poetry](https://img.shields.io/badge/Poetry-dependency%20management-blue)
![License](https://img.shields.io/badge/license-MIT-green)

<img src="ask_petra/image/petra.jpg" alt="Petra" width="300" />

## **P**roject **R**isk **E**valuation and **T**esting **A**ssistant (Petra)

An AI-powered chatbot named Petra that serves the team. Petra combines a curated FAQ knowledge base with Claude AI to provide helpful, cat-personality responses to team questions.

## ✨ Features

- 🤖 **Hybrid RAG System**: Vector search through FAQ data with Claude AI fallback
- 📊 **Streamlit Web Interface**: Interactive chat interface  
- 🐱 **Personality**: Petra maintains a friendly cat personality (ends responses with "Meow")
- 🔍 **Smart Search**: Uses sentence transformers for semantic FAQ matching
- ⚡ **Fast Responses**: Instant replies for known FAQs, intelligent responses for new questions
- 🏢 **Business Context**: Specialized knowledge about risk modeling team operations


### How It Works

1. **User Input** → Streamlit interface captures questions
2. **Vector Search** → Sentence transformer finds similar FAQ entries
3. **Threshold Check** → If similarity score ≥ 0.75, return FAQ answer
4. **Claude Fallback** → If no good match, Claude generates contextual response
5. **Response** → Delivered with Petra's signature cat personality

## 🚀 Quick Start

### Running the Application

```bash
streamlit run app/main.py

# Or run directly
poetry run streamlit run app/main.py
```

The app will be available at `http://localhost:8501`


## 🎯 Usage Examples

### Basic Interaction
```
User: "Hello"
Petra: "meow"
```

### FAQ Query
```
User: "Who are you?"
Petra: "I am a chatbot. My name is Petra and I work for modeling team. Meow."
```

### Business Question (Claude Fallback)
```
User: "What's the latest on the actuarial models?"
Petra: "[Claude-generated response about actuarial models] Meow."
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and test thoroughly
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Open a Pull Request

