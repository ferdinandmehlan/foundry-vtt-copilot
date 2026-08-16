from functools import lru_cache

from agno.db.sqlite import SqliteDb
from agno.memory import MemoryManager

from config import DB_PATH
from model import build_model


@lru_cache(maxsize=1)
def build_db() -> SqliteDb:
    return SqliteDb(db_file=str(DB_PATH))


@lru_cache(maxsize=1)
def build_memory_manager() -> MemoryManager:
    return MemoryManager(
        model=build_model(),
        db=build_db(),
        delete_memories=True,
    )
