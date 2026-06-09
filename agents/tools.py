from duckduckgo_search import DDGS
from langchain.tools import tool


@tool
def web_search(query: str):
    """
    Search the web.
    """

    results = DDGS().text(query, max_results=5)

    text = ""

    for r in results:
        text += f"{r['title']}\n"
        text += f"{r['body']}\n\n"

    return text
