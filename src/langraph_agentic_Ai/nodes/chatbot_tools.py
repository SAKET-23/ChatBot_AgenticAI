from src.langraph_agentic_Ai.state.state import State
from src.langraph_agentic_Ai.tools.search_tool import create_tool_node

class ChatBotNodeWithTools:
    """
    Chatbot implementation with tools
    """
    def __init__(self , model):
        self.llm = model
        
    def process(self, state : State) -> dict:
        
        user_input = state["messages"][-1] if state["messages"] else ""
        llm_response = self.llm.invoke({"role" : "user" , "content" : user_input})
        tool_response = f"Tools integration for: {user_input}"
        
        return {"messages" : [llm_response , tool_response]}
    
    def create_chat_bot(self, tools):
        llm_with_tools = self.llm.bind_tools(tools)
        
        def chat_bot_node(state: State):
            """
            ChatBot logic for processing the input state 
            """
            return {"messages" : [llm_with_tools.invoke(state["messages"])]}
        return chat_bot_node
    