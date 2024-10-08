from fastapi import FastAPI

from prompt.prompt import get_sentiment_classifier_prompt
from llm_service.llm_caller import LLMCaller
from config import LLMConfig, load_yaml_config


app = FastAPI()

message = "อาหารรสชาตห่วยแตก"
sentiment_classifier_prompt = get_sentiment_classifier_prompt(message=message)
load_yaml_config("./config/gemini_config.yaml")
llm_config = LLMConfig()
llm_service = LLMCaller(llm_config)
ans = llm_service.call(sentiment_classifier_prompt)