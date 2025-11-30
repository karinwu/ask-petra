import os
import streamlit as st

from ask_petra.chatbot_core import chatbot_rag


st.image(
    os.path.join("../ask_petra/image/petra.jpg"),
    caption="Petra",
    width=300
)
st.markdown(
    "<h2 style='text-align: center;'>It's pawsome today!</h2>",
    unsafe_allow_html=True
)

st.markdown("### ")
user_input = st.text_input("Meow, I am Petra. How can I help you today?")

if st.button("Ask Petra"):
    if user_input.strip() == "":
        st.warning("Please type a question!")
    else:
        with st.spinner("Petra is thinking..."):
            answer = chatbot_rag(user_input)
            st.markdown(f"**Petra:** {answer}")
