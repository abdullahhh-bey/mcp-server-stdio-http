from dotenv import load_dotenv
from langchain_groq import ChatGroq

#Just testing the GROKAPI key
load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0
)

response = llm.invoke(
    "What is Model Context Protocol? Explain in 2 lines."
)

print(response.content)