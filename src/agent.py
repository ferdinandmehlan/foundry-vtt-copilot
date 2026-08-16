from agno.agent import Agent
from agno.team import Team

from database import build_db, build_memory_manager
from model import build_model
from skills import VaultSkill, build_skills
from tools import (
    build_editor_tools,
    build_read_tools,
)


def build_team() -> Team:
    model = build_model()
    db = build_db()
    memory_manager = build_memory_manager()

    # Specialist: Worldbuilder
    worldbuilder_agent = Agent(
        id="worldbuilder",
        name="Worldbuilder",
        role="Manages atlas/, cast/, codex/, factions/, faiths/, and races/.",
        instructions="""
        You manage the world-building knowledge base for a VTT campaign, maintaining structured Markdown files across atlas (places), cast (characters), codex (lore), factions (organizations), faiths (religions), and races (ancestries).
        
        - Follow the vault-core skill for all global conventions (file naming, frontmatter, wikilinks, GM secrets, content structure).
        - Load the relevant category skill (atlas-manage, cast-manage, codex-manage, factions-manage, faiths-manage, races-manage) for entry-specific rules and templates.
        - Always search the vault for existing entries before creating new ones to avoid duplicates.
        - Cross-link every mentioned entity with [[wikilinks]].
        """,
        skills=build_skills(*VaultSkill),
        tools=[build_editor_tools()],
    )

    # Team Leader / Router
    return Team(
        id="vault-leader",
        name="Vault Lead Copilot",
        model=model,
        instructions=[
            "Delegate tasks to the appropriate specialist based on the vault directory involved.",
            "Ensure all modified or created files follow the vault-core skill.",
        ],
        members=[worldbuilder_agent],
        skills=build_skills(VaultSkill.VAULT_CORE),
        tools=[build_read_tools()],
        db=db,                          # persistence
        memory_manager=memory_manager,  # long term memory
        update_memory_on_run=True,      # update long term memory
        add_history_to_context=True,    # session memory
        num_history_runs=5,             # add last 5 results to next run
        markdown=True,                  # encourages well formatted markdown output
    )
