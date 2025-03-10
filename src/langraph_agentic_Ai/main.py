from src.langraph_agentic_Ai.ui.streamlit_ui.display_result import DisplayResultStreamlit
from src.langraph_agentic_Ai.ui.streamlit_ui.loadui import LoadStreamlitUi
from src.langraph_agentic_Ai.LLMS.groqllm import GroqLLM
from src.langraph_agentic_Ai.graph.graph_builder import GraphBuilder
import streamlit as st
import json

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This function initializes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while 
    implementing exception handling for robustness.
    """
    
    ui = LoadStreamlitUi()
    user_input = ui.load_streamlit_ui()
    
    if not user_input:
        st.error("Error: Failed to load the user input from the UI")
        return

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    elif st.session_state.IsSDLC:
        user_message = st.session_state.state
    else:
         user_message = st.chat_input("Enter your Message")
    
    if user_message:
        try:
            # Loading the LLM
            obj_llm = GroqLLM(user_controls=user_input)
            model = obj_llm.get_llm_models()
            
            if not model:
                st.error("ERROR: Model Not Selected")
                return 
            usecase = user_input.get('selected_usecase')
            if not usecase:
                st.error("ERROR: Usecase Not Selected")
                return 
            # Graph Builder
            graph_builder = GraphBuilder(model)
            
            try:
                graph_builder.setup_graph(usecase)
                DisplayResultStreamlit.display_result_on_ui(usecase , graph_builder , user_message)
            except Exception as e:
                st.error(f"Error: Graph Execution failed with Exception : {e}")
                return
        except Exception as e:
            raise ValueError(f"Error Occure with Exception : {e}")
        
    
            
