import streamlit as st
from chatbot.core import get_response

# Streamlit app configuration
st.set_page_config(page_title="Simple Chatbot", layout="centered")

st.title("🤖 Chatbot")

# Input text box for user input
user_input = st.text_input("Ask me anything:", placeholder="Type your question here...")

if user_input:
    with st.spinner("Thinking..."):
        response = get_response(user_input)
    st.text_area("Chatbot Response:", response, height=200)

