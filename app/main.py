import os
import streamlit as st

from ask_petra.chatbot_core import chatbot_rag


header_col1, header_spacer, header_col2 = st.columns([3, 1, 4])

with header_col1:
    st.image(
        os.path.join("..", "image/petra.jpg"),
        caption="Petra",
        width=300
    )

with header_spacer:
    st.write("")

with header_col2:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown(
        "<h4 style='text-align: left; margin-left: 20px; "
        "font-size: 2.3rem; white-space: nowrap;'>"
        "It's pawsome today!</h4>",
        unsafe_allow_html=True
    )

st.markdown("### ")


with st.form(key='chat_form', clear_on_submit=True):
    col1, col2 = st.columns([1, 8])

    with col1:
        st.image(
            os.path.join("..", "image/petra.jpg"),
            width=50
        )

    with col2:
        user_input = st.text_input(
            "Meow, I am Petra. How can I help you today?",
            label_visibility="visible"
        )

    submitted = st.form_submit_button("Ask Petra")

if submitted:
    if user_input.strip() == "":
        st.warning("Please type a question!")
    else:
        with st.spinner("Petra is thinking..."):
            answer = chatbot_rag(user_input)
            st.markdown(f"**Petra:** {answer}")
