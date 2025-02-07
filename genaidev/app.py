#!/ai/genaidev/bin/python3
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI client with the API key from environment variables
client = OpenAI(
    api_key=os.getenv("OPENAI_KEY"),
)

llm_openai = ChatOpenAI(model="gpt-4o", api_key=client.api_key)
st.title("Q & A With AI")

question = st.text_input("Your Question")
if question:
    response = llm_openai.invoke(question)
    st.write(response.content)
