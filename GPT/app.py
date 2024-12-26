from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

# Load environment variables
load_dotenv()

# Set up API keys
groq_api_key = os.getenv("GOQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="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"
LANGCHAIN_PROJECT="pr-enchanted-casserole-97"
# Initialize Langchain Google Generative AI model
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage

def get_response(question):
    chatllm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0.5,  # Adjusted temperature for variety
        max_tokens=150,   # Set max tokens to avoid None issues
        timeout=None,
        max_retries=2,
    )
    response = chatllm([HumanMessage(content=question)])
    return response

# Streamlit UI setup
st.set_page_config(page_title="QA BOT")

# Input field for user question
input_text = st.text_input("Input: ", key="input")

# Submit button for generating response
submit = st.button("Ask Question")

if submit:
    if input_text:  # Ensure there is input
        response = get_response(input_text)  # Get the response
        st.subheader("The response is:")
        
        # Check if response has content
        if response and response.content:
            st.write(response.content)  # Display the response content
        else:
            st.write("No content received. Please try a different question.")  # Fallback message
    else:
        st.write("Please enter a question.")