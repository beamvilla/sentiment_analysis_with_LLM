import os
import time
import google.generativeai as genai
from typing import Mapping, Any
from ratelimit import limits, sleep_and_retry

from logger import service_log
from .core import CoreService


global N_LIMIT_REQUEST, LIMIT_PERIOD
N_LIMIT_REQUEST = 60
LIMIT_PERIOD = 60


class GeminiService(CoreService):
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        self.set_env(llm_config)
    
    def set_env(self, llm_config: Mapping[str, Any]):
        self.llm_config = llm_config
        gemini_api_key = os.environ["GEMINI_API_KEY"]
        genai.configure(api_key=gemini_api_key)
        self.safety_settings=[
                    {
                        "category": "HARM_CATEGORY_DANGEROUS",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_HARASSMENT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_HATE_SPEECH",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                        "threshold": "BLOCK_NONE",
                    },
                    {
                        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                        "threshold": "BLOCK_NONE",
                    }
                ]
        self.generation_config = genai.types.GenerationConfig(temperature=self.llm_config.TEMPERATURE)
        self.model = genai.GenerativeModel(self.llm_config.MODEL)

    @sleep_and_retry
    @limits(calls=N_LIMIT_REQUEST, period=LIMIT_PERIOD)
    def call(self, prompt: str) -> str:
        try_connect = 0
        while True:
            try:
                response = self.model.generate_content(
                                prompt,
                                generation_config=self.generation_config,
                                safety_settings=self.safety_settings
                            )
            except Exception as err:
                service_log().error(f"{self.llm_config.MODEL} request error: {err}, waiting for connecting to {self.llm_config.MODEL} again")
                time.sleep(self.llm_config.RETRY_WAITING)
                try_connect += 1
                if try_connect > self.llm_config.LIMIT_CONNECT:
                    service_log().error(f"Can't connect to {self.llm_config.MODEL}")
                    raise
                continue

            try:
                ans = response.text
            except Exception as err:
                try:
                    for candidate in response.candidates:
                        return str([part.text for part in candidate.content.parts])
                except Exception as err:
                    service_log().error(f"Got invalid answer format: {ans}, with error: {err}")
                    raise
            return ans
