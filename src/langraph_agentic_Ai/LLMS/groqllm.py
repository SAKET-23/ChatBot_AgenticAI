import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self , user_controls):
        self.user_control = user_controls
        
    def get_llm_models(self):
        try:    
            groq_api = self.user_control["GROQ_API_KEY"]
            selected_groq_model = self.user_control["selected_groq_model"]
            if groq_api == '' and os.environ["GROQ_API_KEY"] == '':
                st.error("!!ERROR : ENTER THE API KEY")
            llm = ChatGroq(api_key=groq_api , model= selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error occured with Exception : {e}")
        return llm
        