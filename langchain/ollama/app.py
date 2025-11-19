# setup key environment
import  os
from dotenv import load_dotenv
load_dotenv()

from langchain_community.llms import Ollama


 
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate

from langchain_core.output_parsers import StrOutputParser
# langsmith tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="True"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


# design my prompt template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant . please respond to the question asked."),
        ("user","questin:{question}")
    ]
)

# design streamlit framework
st.title(" Langchain Demo With LLAMA3")
input_text=st.text_input("what question you have in mind?")


# ollma Llama3 model

llm = Ollama(model="llama3")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    response=chain.invoke({"question":input_text})
    st.write(response)