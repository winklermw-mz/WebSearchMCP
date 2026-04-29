from fastmcp import FastMCP
from datetime import datetime
from typing import Annotated
from tools.duckduckgo import web_search
from tools.wiki import query_wikipedia
from utils.config import SERVER_IP, SERVER_PORT, MY_LOCATION


mcp = FastMCP("MyMCP")

@mcp.tool(description="To query unknown or recent data this tool can be used to search the internet")
def search_web(query: str) -> str:
    try:
        return web_search(query)
    except Exception as e:
        return f"Something went wrong: {e}"
    
@mcp.tool(description="Get more information about a specific topic from Wikipedia to answer the user query")
def search_wikipedia(
    topic: Annotated[str, "Topic to be searched for in Wikipedia. Since only one topic can be selected, it should be as concise as possible. For example, 'London' if you are looking for sights in London."], 
) -> str:
    return query_wikipedia(topic, "de")

@mcp.tool(description="Returns the current date")
def get_current_date() -> str:
    current_date = datetime.now().strftime("%A, %B %d, %Y")
    return f"Today's date is {current_date}"

@mcp.tool(description="Returns the current location of the user")
def get_current_location() -> str:
    return f"The user is located in {MY_LOCATION}"


if __name__ == "__main__":
    mcp.run(transport="http", host=SERVER_IP, port=SERVER_PORT)