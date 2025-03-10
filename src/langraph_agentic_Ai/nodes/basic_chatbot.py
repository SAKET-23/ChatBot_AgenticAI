from src.langraph_agentic_Ai.state.state import State

class BasicChatBotNode:
    """
    Basic Chatbot implementation
    """
    def __init__(self , model):
        self.llm = model
        
    def process(self, state : State) -> dict:
        return {"messages" : self.llm.invoke(state["messages"])}
    