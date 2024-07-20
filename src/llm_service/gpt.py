import openai
import os
from typing import Mapping, Any
import time

from logger import service_log


class GPTService:
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        self.set_env(llm_config)
    
    def set_env(self, llm_config: Mapping[str, Any]):
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
                service_log().error(f"Openai request error: {err}, waiting for connecting to {self.llm_config.MODEL} again")
                time.sleep(self.llm_config.RETRY_WAITING)
                try_connect += 1
                if try_connect > self.llm_config.LIMIT_CONNECT:
                    service_log().error(f"Can't connect to {self.llm_config.MODEL}")
                    raise
                service_log().info(f"retry to connect {self.llm_config.MODEL} round {try_connect}")
                continue
            
            try:
                ans = str(completion.choices[0].message.content)
            except Exception as err:
                service_log().error(f"Got invalid answer format: {completion}, with error: {err}")
                raise
            return ans