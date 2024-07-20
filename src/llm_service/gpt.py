import openai
import os
from typing import Mapping, Any
import time
from ratelimit import limits, sleep_and_retry

from logger import service_log
from .core import CoreService



global N_LIMIT_REQUEST, LIMIT_PERIOD
N_LIMIT_REQUEST = 120
LIMIT_PERIOD = 60


class GPTService(CoreService):
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        self.set_env(llm_config)
    
    def set_env(self, llm_config: Mapping[str, Any]):
        self.llm_config = llm_config
        openai.api_key = os.getenv("OPENAI_API_KEY")
        openai.api_requestor.TIMEOUT_SECS = 60
    
    @sleep_and_retry
    @limits(calls=N_LIMIT_REQUEST, period=LIMIT_PERIOD)
    def call(self, prompt: str) -> str:
        try_connect = 0
        while True:
            try:
                completion = openai.ChatCompletion.create(
                                    model=self.llm_config.MODEL,
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
                continue
            
            try:
                ans = str(completion.choices[0].message.content)
            except Exception as err:
                service_log().error(f"Got invalid answer format: {completion}, with error: {err}")
                raise
            return ans