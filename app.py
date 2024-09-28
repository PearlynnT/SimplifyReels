import streamlit as st
from chatbot import chat

st.title("Simplify Reels")
page_bg_img = """<style> 
[data-testid="stAppViewContainer"]  
{ background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); 
background-size: cover; }  

</style>"""

st.markdown(page_bg_img, unsafe_allow_html=True)

prompt = st.chat_input("Say something")
if prompt:
    with st.spinner("Generating your queries..."):  # Show loading spinner
        chat(prompt)# Creates chat_output.txt
    # The rest of backend goes here
