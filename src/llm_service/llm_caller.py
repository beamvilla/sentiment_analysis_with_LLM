from typing import Mapping, Any
from dotenv import load_dotenv


class LLMCaller:
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        load_dotenv()
        self.set_llm_service(llm_config)
        
    def set_llm_service(self, llm_config: Mapping[str, Any]):
        self.llm_config = llm_config
        if "gpt" in self.llm_config.MODEL:
            from .gpt import GPTService
            self.llm_service = GPTService(self.llm_config)
        elif "gemini" in self.llm_config.MODEL:
            from .gemini import GeminiService
            self.llm_service = GeminiService(self.llm_config)
    
    def call(self, prompt: str) -> str:
        return self.llm_service.call(prompt=prompt)