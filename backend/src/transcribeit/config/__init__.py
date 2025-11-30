from .environment import EnvVarConfig
from ..helpers.singleton import singleton
import whisper


@singleton
class AppConfig:
    def __init__(self):
        self.env: EnvVarConfig = EnvVarConfig()
        self.whisper_model = whisper.load_model("tiny")

def get_config() -> AppConfig:
    return AppConfig()