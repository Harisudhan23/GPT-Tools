from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from PIL import Image
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro')

def get_gemini_response(input, image, prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        
        bytes_data = uploaded_file.getvalue()

        images_parts = [
            {
                "mime_type": uploaded_file.type, 
                "data": bytes_data
            }
        ]
        return images_parts
    else:
        raise FileNotFoundError("No file uploaded")

#Initialize streamlit app
st.set_page_config(page_title="Multilanguage Invoice Extractor")
input = st.text_input("Input Prompt:", key='input')
uploaded_file = st.file_uploader("Choose an image of an invoice... ", type=["jpg","jpeg","png"])
image =""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the invoice")

input_prompt = """
You are an expert in understanding invoices. We will upload an image as invoice and you will have
to answer any questions based on the uploaded invoice image
"""
if submit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data,input)
    st.subheader("The Response is")
    st.write(response)

    