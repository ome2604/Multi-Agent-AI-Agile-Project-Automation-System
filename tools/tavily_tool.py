from tavily import TavilyClient

from orchestrator.config import TAVILY_API_KEY


client = TavilyClient(
    api_key=TAVILY_API_KEY
)


def search_web(query):

    response = client.search(
        query=query,
        search_depth="basic"
    )

    return response