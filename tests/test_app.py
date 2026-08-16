import re

from agno.tools.file import FileTools
from fastapi.testclient import TestClient

from agent import EDITOR_INSTRUCTIONS, VAULT_INSTRUCTIONS, build_team
from app import app


def _file_tools(tools):
    return [t for t in tools if isinstance(t, FileTools)]


def test_app_starts():
    client = TestClient(app)
    response = client.get("/openapi.json")
    assert response.status_code == 200

    schema = response.json()
    assert "paths" in schema
    assert "/" in schema["paths"]
    assert "get" in schema["paths"]["/"]


def test_team_loads_skills():
    team = build_team()
    assert set(team.skills.get_skill_names()) == {
        "audit-vault",
        "create-location-hierarchy",
        "create-npc",
        "create-world-entity",
        "index-synchronizer",
        "log-session",
        "prep-encounter",
        "vault-structure-guide",
    }


def test_vault_structure_guide_is_loadable():
    team = build_team()
    skill = team.skills.get_skill("vault-structure-guide")
    assert skill is not None
    assert "world/countries" in skill.instructions
    assert "index-synchronizer" in skill.instructions


def test_vault_structure_guide_resolves_hub_and_active_campaign():
    team = build_team()
    skill = team.skills.get_skill("vault-structure-guide")
    assert "`_index.md`" in skill.instructions
    assert "status: active" in skill.instructions
    assert not re.search(r"(?<![_-])index\.md", skill.instructions)


def test_vault_structure_guide_forbids_host_absolute_paths():
    team = build_team()
    skill = team.skills.get_skill("vault-structure-guide")
    assert "host-absolute" in skill.instructions


def test_leader_instructions_enforce_index_sync():
    assert "index-synchronizer" in VAULT_INSTRUCTIONS
    assert "ALWAYS call" in VAULT_INSTRUCTIONS
    assert "Never improvise" in VAULT_INSTRUCTIONS


def test_leader_instructions_structured_delegation():
    assert "structured spec" in VAULT_INSTRUCTIONS
    assert "one entity per call" in VAULT_INSTRUCTIONS


def test_editor_instructions_structured_specs():
    assert "Structured entity specs" in EDITOR_INSTRUCTIONS
    assert "templates/" in EDITOR_INSTRUCTIONS


def test_leader_is_read_only():
    team = build_team()
    file_tools = _file_tools(team.tools)[0]
    tool_names = set(file_tools.functions.keys())
    expected = {
        "read_file",
        "read_file_chunk",
        "list_files",
        "search_files",
        "search_content",
    }
    assert expected <= tool_names
    assert "save_file" not in tool_names
    assert "replace_file_chunk" not in tool_names
    assert "delete_file" not in tool_names


def test_editor_member_has_write_tools():
    team = build_team()
    editor = next(m for m in team.members if m.id == "vault-editor")
    file_tools = _file_tools(editor.tools)[0]
    tool_names = set(file_tools.functions.keys())
    expected = {"save_file", "replace_file_chunk", "read_file", "read_file_chunk"}
    assert expected <= tool_names
    assert "search_files" not in tool_names
    assert "delete_file" not in tool_names
