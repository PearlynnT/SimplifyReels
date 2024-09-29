import streamlit as st
from chatbot import chat
import os
import time

st.title("Simplify Reels")
# page_bg_img = """<style> 
# [data-testid="stAppViewContainer"]  
# { background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366"); 
# background-size: cover; }  

# </style>"""

# st.markdown(page_bg_img, unsafe_allow_html=True)

video_file = "output_video.mp4"

# Handle user input
prompt = st.chat_input("Say something")
if prompt:
    # Remove the existing video file if it exists
    if os.path.exists(video_file):
        os.remove(video_file)
    last_modified_time = None
    with st.spinner("Generating your queries..."):  # Show loading spinner
        chat(prompt)  # Creates chat_output.txt
    with st.spinner("Generating your video..."):
        while True:
            if os.path.exists(video_file):
                current_modified_time = os.path.getmtime(video_file)

                # Check if the video file has stopped modifying
                if current_modified_time != last_modified_time:
                    last_modified_time = current_modified_time
                    time.sleep(10) 
                else:
                    st.video(video_file)
                    break  # Exit the loop after displaying the video
            else:
                time.sleep(10)  
