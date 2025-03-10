pip install openai streamlit


import openai
import streamlit as st

# Set up OpenAI API (Replace "YOUR_OPENAI_API_KEY" with your actual API key)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Function to generate AI response
def get_ai_response(user_input):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a compassionate and friendly counselor chatbot that helps users with anxiety, depression, and self-doubt."},
                      {"role": "user", "content": user_input}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return "I'm here to help, but I encountered an issue. Please try again later!"

# Streamlit UI
st.title("🌿 AI Counselor: Your Friendly Support Chatbot")
st.write("Hello! I'm here to help you through your difficult moments. You can share your thoughts, and I'll do my best to support you.")

# User input
user_input = st.text_input("How are you feeling today?")

if user_input:
    response = get_ai_response(user_input)
    st.write("🧡 Chatbot:", response)

# Some helpful tips for mental well-being
st.subheader("💡 Self-Help Tips")
st.write("✔ Practice deep breathing exercises 🧘‍♂️")  
st.write("✔ Talk to a trusted friend or family member 🗣")  
st.write("✔ Engage in activities that make you happy 🎨📚")  
st.write("✔ Remember, you are not alone. Seeking help is a sign of strength! 💪")  
