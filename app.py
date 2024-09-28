import streamlit as st

st.title("Simplify Reels")

# Initialize session state to store chat messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to add user input to the chat
def add_message():
    user_input = st.text_input("Type your message here:", "")
    if st.button("Send") and user_input:
        st.session_state.messages.append(user_input)
        st.session_state.user_input = ""  # Clear input after sending

# Display chat messages
for message in st.session_state.messages:
    continue # placeholder

# Add new message input
add_message()