#!/ai/genaidev/bin/python3
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from openai import OpenAI
from langchain.prompts import PromptTemplate
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize OpenAI client with the API key from environment variables
client = OpenAI(
    api_key=os.getenv("OPENAI_KEY"),
)

# Create an object of PromtTemplate

prompt = PromptTemplate(input_variables=["country"], template="what is the currency of {country}? Answer in one short paragraph",)


llm_openai = ChatOpenAI(model="gpt-4o", api_key=client.api_key)
st.title("Q & A With AI")

country = st.text_input("Input country")

if country:
    response = llm_openai.invoke(prompt.format(country=country))
    st.write(response.content)
