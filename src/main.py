from prompt.prompt import get_sentiment_classifier_prompt
from llm_service.llm_caller import LLMCaller
from config import LLMConfig, load_yaml_config


sentiment_classifier_prompt = get_sentiment_classifier_prompt(message="อาหารรสชาตห่วยแตก")
load_yaml_config()
llm_config = LLMConfig()
llm_service = LLMCaller(llm_config)
ans = llm_service.call(sentiment_classifier_prompt)
print(ans)