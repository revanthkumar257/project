from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the Google Generative AI API with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the Gemini Model and get responses
model = genai.GenerativeModel("gemini-pro")

def generate_text(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def is_airbnb_related(question):
    # Define keywords related to Airbnb
    airbnb_keywords = [
        "Airbnb", "booking", "reservation", "host", "guest", 
        "policy", "payment", "refund", "safety", "trust", "stay", 
        "property", "cancellation", "review", "check-in", "check-out"
    ]
    # Check if the question contains any Airbnb-related keywords
    return any(keyword.lower() in question.lower() for keyword in airbnb_keywords)

# Creating a frontend application with minimal code
st.set_page_config(page_title="Airbnb Bot")
st.title("Airbnb Help Bot")
st.header("Ask for Airbnb Help")

# User instructions and examples
st.markdown("""
Welcome to the Airbnb Help Bot! You can ask me questions related to:
- Booking a stay
- Cancelling a reservation
- Host and guest policies
- Payment and refund issues
- Safety and trust

**Examples:**
- How do I book a stay on Airbnb?
- What is the cancellation policy for hosts?
- How can I contact Airbnb customer support?
""")

# User input
user_input = st.text_input("Ask your Airbnb question here:", key="input")
submit = st.button("Get Response")

if submit and user_input:
    if is_airbnb_related(user_input):
        with st.spinner("Generating response..."):
            response = generate_text(user_input)
        st.subheader("The response is:")
        st.write(response)
    else:
        st.subheader("The response is:")
        st.write("This bot only handles Airbnb-related questions. Please ask a question related to Airbnb.")
