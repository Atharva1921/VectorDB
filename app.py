from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st


prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant named aura.Please respond to the user queries"),
        ("user","Question:{question}")
    ]
)


st.title('Langchain Demo with Ollama')
input_text = st.text_input("Search the topic u want")