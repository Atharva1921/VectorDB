from langchain_community.llms import Ollama
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import LLMChain


import streamlit as st


def readPDF(name):

    loader = PyPDFLoader(name)
    pages = loader.load_and_split()
    return pages

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a Resume text summarizer. I will provide you resume in text format."),
        ("user","Help me segrigate the following resume information in three categories name, personal details and professional summary. \n RESUME: {resume}")
    ]
)

llm = Ollama(model="llama3.1:8b")
outputParser = StrOutputParser()
chain = prompt | llm | outputParser

st.title('Langchain Demo with Ollama')

uploaded_file = st.file_uploader("Upload Resume", type="pdf")
if uploaded_file:
    
    temp_file = "./temp.pdf"
    with open(temp_file, "wb") as file:
        file.write(uploaded_file.getvalue())
        file_name = uploaded_file.name
        file.close()

    document = readPDF("sample.pdf")

    

if st.button("Summarize"):
    st.write(chain.invoke({"resume": document[0].page_content}))    


