from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI()

question = input()

prompt = ChatPromptTemplate.from_messages([
    ("system", "")
])