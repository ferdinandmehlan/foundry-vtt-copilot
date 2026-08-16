from functools import lru_cache
from tempfile import TemporaryDirectory

from agno.models.openai import OpenAIChat

from config import settings


@lru_cache(maxsize=1)
def build_model() -> OpenAIChat:
    with TemporaryDirectory() as cache_dir:
        return OpenAIChat(
            id=settings.model_name,
            base_url=settings.openai_base_url,
            api_key=settings.openai_api_key,
            cache_response=True,
            cache_dir=cache_dir,
        )
