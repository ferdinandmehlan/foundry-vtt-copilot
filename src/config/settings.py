from pathlib import Path
from typing import ClassVar

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()

PROJECT_ROOT = Path(__file__).parent.parent.parent.resolve()
DB_PATH = PROJECT_ROOT / "data" / "fvtt-copilot.db"
VAULT_DIR = PROJECT_ROOT / "data" / "vault"
SKILLS_DIR = PROJECT_ROOT / "src" / "skills"


class Settings(BaseSettings):
    host: str = "127.0.0.1"
    port: int = 8001
    reload: bool = True

    openai_base_url: str = ""
    openai_api_key: str = ""
    model_name: str = ""

    model_config: ClassVar[SettingsConfigDict] = SettingsConfigDict(env_prefix="")
