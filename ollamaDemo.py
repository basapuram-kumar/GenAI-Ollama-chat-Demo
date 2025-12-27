import os
from dotenv import load_dotenv

from langchain_community.llms import  ollama
import streamlit as st
from langchain_community.llms.ollama import Ollama
from langchain_core.prompts.chat import  ChatPromptTemplate
from langchain_core.output_parsers import  StrOutputParser


load_dotenv()
#
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# os.environ["LANGCHAIN_TRACING_V2"]="true"
# os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt= ChatPromptTemplate.from_messages((
    [
        ("system", "You are a helpful assistant. Please respond to the question asked"),
        ("user", "Question: {question}")
    ]
))

## Streamlit Framework
st.title("Langchain Demo using LLAMA-3 model")

input_text=st.text_input("Enter your question here:")

###   Ollama model
llm=Ollama(model='llama3.1:8b')

output_parser =StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
