from typing import Mapping, Any


class CoreService:
    def __init__(self, llm_config: Mapping[str, Any]) -> None:
        pass

    def set_env(self, llm_config: Mapping[str, Any]):
        pass

    def call(self, prompt: str) -> str:
        pass