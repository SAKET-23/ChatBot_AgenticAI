from configparser import ConfigParser

class Config:
    def __init__(self , config_file = "./src/langraph_agentic_Ai/ui/ui_config_file.ini"):
        self.config = ConfigParser()
        self.config.read(config_file)
        
    def get_llm_option(self):
        return self.config["DEFAULT"].get("LLM_OPTIONS").split(", ")
    
    def get_usecase_option(self):
        return self.config["DEFAULT"].get("USECASE_OPTIONS").split(", ")
    
    def get_groq_model_option(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPTIONS").split(", ")
    
    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE") 