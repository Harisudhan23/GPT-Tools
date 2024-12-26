
import streamlit as st
import os
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def get_genai_response(question):
    # Retrieve API key from environment variables
    google_api_key = os.getenv("GOOGLE_API_KEY")
    
    # Initialize the language model with the API key
    llm = ChatGoogleGenerativeAI(google_api_key=google_api_key, model="gemini-1.5-flash", temperature=0.5)  # Updated model name
    
    # Format the input as a list of messages
    messages = [{"role": "user", "content": question}]
    
    # Get the response from the model
    response = llm.invoke(messages=messages)
    
    # Return the response content
    return response.get("content", "No response received.")

# Streamlit app setup
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Application")

# User input field
input_question = st.text_input("Input:", key='input')

# Process when the button is clicked
if st.button("Submit"):
    if input_question.strip():  # Check if the input is not empty
        try:
            # Get the response from the model
            response = get_genai_response(input_question)
            st.subheader("The Response is:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.error("Please enter a valid question.")
