from langgraph.graph import StateGraph, START,END, MessagesState
from langgraph.prebuilt import tools_condition,ToolNode
from langchain_core.prompts import ChatPromptTemplate
from src.langraph_agentic_Ai.state.state import State
from src.langraph_agentic_Ai.nodes.basic_chatbot import BasicChatBotNode
from src.langraph_agentic_Ai.nodes.chatbot_tools import ChatBotNodeWithTools
from src.langraph_agentic_Ai.tools.search_tool import get_tools , create_tool_node
from langgraph.prebuilt import tools_condition

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)
        
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the `BasicChatbotNode` class 
        and integrates it into the graph. The chatbot node is set as both the 
        entry and exit point of the graph.
        """
        
        self.basic_chatbot_node = BasicChatBotNode(self.llm)
        self.graph_builder.add_node("chatbot" , self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_edge("chatbot" , END)
    
    def chatbot_with_tool_build_graph(self):
        """
        Builds a chatbot with tools graph using LangGraph.
        This method initializes a chatbot node using the `ChatBotNodeWithTools` class 
        and integrates it into the graph. The chatbot node is set as the 
        entry and tools as the exit point of the graph.
        """
        tools = get_tools()
        tools_node  = create_tool_node(tools)
        self.chatbot_tools_node = ChatBotNodeWithTools(self.llm)
        self.chatbotnode = self.chatbot_tools_node.create_chat_bot(tools)
        self.graph_builder.add_node("chatbot" , self.chatbotnode)
        self.graph_builder.add_node("tools" , tools_node)
        
        self.graph_builder.add_edge(START , "chatbot")
        self.graph_builder.add_conditional_edges("chatbot" , tools_condition)
        self.graph_builder.add_edge("tools" , END)
        
    def setup_graph(self, usecase: str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Tool":
            self.chatbot_with_tool_build_graph()
        return  self.graph_builder.compile()


    
        