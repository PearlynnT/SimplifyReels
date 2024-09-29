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
def local_css():
    st.markdown("""
    <style>
    /* Background */
    [data-testid="stAppViewContainer"] {
        background-color: #3E2723; /* Dark Brown */
        color: #F5F5F5; /* Light Gray for text */
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #4E342E; /* Slightly lighter brown */
    }

    /* Title */
    h1 {
        color: #FF6F00; /* Orange */
        font-family: 'Cinzel', serif; /* Western-style font */
        text-align: center;
        text-shadow: 2px 2px #000000;
    }

    /* Chat Input */
    .css-1r6slb0 {
        background-color: #5D4037; /* Brown */
        color: #F5F5F5;
    }

    /* Buttons */
    .css-1emrehy.edgvbvh3 {
        background-color: #BF360C; /* Deep Orange */
        color: #FFF3E0;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-family: 'Cinzel', serif;
        box-shadow: 2px 2px #000000;
    }
                
    white-text {
        color: white            
    }
                
    /* Footer */
    footer {
        visibility: hidden;
    }

    /* Import Google Font */
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&display=swap');
    </style>
    """, unsafe_allow_html=True)

local_css()

# Add a greeting message
if 'greeted' not in st.session_state:
    with st.chat_message("🤠"):
        st.write(f":orange[Howdy, partner! Tell me a story and I'll turn it into a video for you.]")
    st.session_state['greeted'] = True

video_file = "output_video.mp4"

# Handle user input
prompt = st.chat_input("Once upon a time...")
if prompt:
    # Remove the existing video file if it exists
    if os.path.exists(video_file):
        os.remove(video_file)
    last_modified_time = None
    with st.spinner("Generating your queries..."):  # Show loading spinner
        chat(prompt)  # Creates chat_output.txt
    with st.spinner("Generating your video..."):
        time.sleep(100) 
        st.video(video_file) 
