import streamlit as st
import os
from datetime import date

from langchain_core.messages import AIMessage, HumanMessage
from src.langraph_agentic_Ai.ui.ui_config_file import Config

class LoadStreamlitUi:
    def __init__(self):
        self.config = Config() # config
        self.user_controls = {}
        
        
        
