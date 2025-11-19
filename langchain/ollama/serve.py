from fastapi import FastAPI

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes  #this add_routes helps to create api
from dotenv import load_dotenv
load_dotenv()

# read api key
groq_api_key=os.getenv("groq_api_key")

# model fit
model=ChatGroq(model="llama-3.1-8b-instant",groq_api_key=groq_api_key)


## use prompt template


generic_template="translate the following into {language}"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","{text}")
    ]
)


parser=StrOutputParser()

# create chian
chain=prompt|model|parser



# add defination
app=FastAPI(title="langchain Server",
         version="1.0",
            description="A simple API server using Langchin runnable interface" 
                )

# adding chain rout
add_routes(

    app,
    chain,
    path="/chain"

)


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="localhost",port=8000)
