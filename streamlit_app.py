import streamlit as st
import openai  # For OpenAI's GPT-based conversation logic

# Load OpenAI API Key from Streamlit Secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit UI Design
st.title("💬 Relationship Advice Chatbot")
st.write("I'm here to provide helpful advice on relationships. Ask me anything!")

# Manage chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
user_input = st.chat_input("What's on your mind?")
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # AI Response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" for enhanced results
            messages=[{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
        )
        bot_response = response["choices"][0]["message"]["content"]

    except Exception:
        bot_response = "Sorry, I'm having trouble right now. Please try again."

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
