import streamlit as st
from chatbot import chat

st.title("Simplify Reels")

prompt = st.chat_input("Say something")
if prompt:
    chat(prompt)
