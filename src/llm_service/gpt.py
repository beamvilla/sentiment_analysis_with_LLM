import openai
import os
from typing import Mapping, Any

from logger import service_log


class GPTService:
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        self.llm_config = llm_config
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_requestor.TIMEOUT_SECS = 60
    
    def call(self, prompt: str) -> str:
        try_connect = 0
        while True:
            try:
                service_log().info(f"Sending a request to {self.llm_config.MODEL}")
                completion = openai.ChatCompletion.create(
                                    model=self.model,
                                    messages=[
                                        {"role": "user", "content": prompt}
                                    ],
                                    max_tokens=self.llm_config.MAX_TOKENS,
                                    temperature=self.llm_config.TEMPERATURE
                                )
            except Exception as err:
                service_log().error(f"Openai request error: {err}, waiting for connecting to openai again")
                try_connect += 1
                if try_connect > self.llm_config.LIMIT_CONNECT:
                    service_log().error("Can't connect to openai")
                    return
                service_log().info(f"retry to connect openai round {try_connect}")
                continue
            
            try:
                ans = str(completion.choices[0].message.content)
            except Exception as err:
                service_log().error(f"Got invalid answer format: {completion}, with error: {err}")
                return None
            return ans