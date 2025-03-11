from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode


def get_tools():
    """
    Return the list of the tools
    """
    tools = [TavilySearchResults(max_results=2)]
    return tools

def create_tool_node(tools):
    """
    Return  a tools node
    """
    return ToolNode(tools=tools)


