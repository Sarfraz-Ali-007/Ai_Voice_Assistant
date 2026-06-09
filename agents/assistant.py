from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

from agents.tools import web_search

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

tools = [web_search]

agent = create_react_agent(
    llm,
    tools
)
