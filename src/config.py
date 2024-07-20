import yaml
from dataclasses import dataclass
from typing import Mapping, Any


@dataclass
class LLMBaseConfig:
    MODEL: str
    CONFIG: Mapping[str, Any]


class LLMConfig:
    def __init__(self, LLM_config_field: str = "LLM_CONFIG") -> None:
        llm_config: Mapping[str, str | Mapping[str, Any]] = LLMBaseConfig(**config[LLM_config_field])

        self.MODEL: str          = llm_config.MODEL
        self.LIMIT_CONNECT: int  = llm_config.CONFIG.get("LIMIT_CONNECT", 3)
        self.TEMPERATURE: float  = llm_config.CONFIG.get("TEMPERATURE", 0.0)
        self.MAX_TOKENS: int     = llm_config.CONFIG.get("MAX_TOKENS", 1024)
        self.RETRY_WAITING: int  = llm_config.CONFIG.get("RETRY_WAITING", 30)


def load_yaml_config(config_path: str = "./config/config.yaml"):
    global config
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)


load_yaml_config()