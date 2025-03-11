import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.langraph_agentic_Ai.ui.ui_config_file import Config

class LoadStreamlitUi:
    def __init__(self):
        self.config = Config() # config
        self.user_controls = {}
    
    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None }
       
    def  load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title() , layout='wide')
        st.header(self.config.get_page_title())
        st.session_state.timeframe = ''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        with st.sidebar:
            
            llm_options = self.config.get_llm_option()
            usecase_options = self.config.get_usecase_option()
            
            self.user_controls["selected_llm"] = st.selectbox("Select LLM" , llm_options)
            if self.user_controls["selected_llm"] == 'Groq':
                # Select Groq Model
                model_options = self.config.get_groq_model_option()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model" , model_options)
                # API KEY
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("API KEY" , type='password')
                
                #Validate the API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("!!!! Enter API KEY !!!!")
            # Use case selection   
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase" , usecase_options)
            if self.user_controls["selected_usecase"] == "Chatbot with Tool": 
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY_API_KEY" , type='password')
                if not self.user_controls["TAVILY_API_KEY"]:
                        st.warning("!!!! Enter TAVILY API KEY !!!!")
            
            if 'state' not in st.session_state:
                st.session_state.state = self.initialize_session()
            
            return self.user_controls
        
    
