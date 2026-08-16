from enum import Enum

from agno.skills import LocalSkills, Skills

from config import SKILLS_DIR


class VaultSkill(str, Enum):
    ATLAS_MANAGE = "atlas-manage"
    CAST_MANAGE = "cast-manage"
    CODEX_MANAGE = "codex-manage"
    FACTIONS_MANAGE = "factions-manage"
    FAITHS_MANAGE = "faiths-manage"
    RACES_MANAGE = "races-manage"
    VAULT_CORE = "vault-core"


def build_skills(*skills: VaultSkill) -> Skills:
    loaders = [LocalSkills(path=str(SKILLS_DIR / s.value)) for s in skills]
    return Skills(loaders=loaders)
