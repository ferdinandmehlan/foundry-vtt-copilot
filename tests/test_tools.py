from pathlib import Path

from tools import VaultFileTools, normalize_vault_path


def test_normalize_absolute_path_under_base_dir(tmp_path):
    base = tmp_path / "vault"
    target = base / "campaign" / "world" / "factions" / "faction_a.md"
    assert (
        normalize_vault_path(base, str(target))
        == "campaign/world/factions/faction_a.md"
    )


def test_normalize_keeps_relative_path(tmp_path):
    path = "campaign/world/factions/faction_a.md"
    assert normalize_vault_path(tmp_path, path) == path


def test_normalize_keeps_outside_absolute(tmp_path):
    outside = str(Path("/tmp") / "elsewhere" / "file.md")
    assert normalize_vault_path(tmp_path, outside) == outside


def test_normalize_handles_spaces_and_empty(tmp_path):
    target = tmp_path / "Spooktober Special" / "world" / "factions" / "faction_a.md"
    assert (
        normalize_vault_path(tmp_path, str(target))
        == "Spooktober Special/world/factions/faction_a.md"
    )
    assert normalize_vault_path(tmp_path, "") == ""
    assert normalize_vault_path(tmp_path, None) is None


def test_vault_file_tools_read_file_absolute_path(tmp_path):
    vault = tmp_path / "vault"
    (vault / "campaign" / "notes").mkdir(parents=True)
    (vault / "campaign" / "notes" / "note.md").write_text("hello world")

    ft = VaultFileTools(base_dir=vault)
    assert "hello world" in ft.read_file(str(vault / "campaign" / "notes" / "note.md"))
    assert "hello world" in ft.read_file("campaign/notes/note.md")


def test_vault_file_tools_save_file_absolute_path(tmp_path):
    vault = tmp_path / "vault"
    (vault / "campaign" / "notes").mkdir(parents=True)

    ft = VaultFileTools(base_dir=vault)
    result = ft.save_file(
        contents="body",
        file_name=str(vault / "campaign" / "notes" / "new.md"),
    )
    assert "campaign/notes/new.md" in result
    assert (vault / "campaign" / "notes" / "new.md").read_text() == "body"


def test_vault_file_tools_replace_chunk_absolute_path(tmp_path):
    vault = tmp_path / "vault"
    (vault / "campaign").mkdir(parents=True)
    (vault / "campaign" / "doc.md").write_text("line1\nline2\nline3\n")

    ft = VaultFileTools(base_dir=vault)
    result = ft.replace_file_chunk(
        file_name=str(vault / "campaign" / "doc.md"),
        start_line=2,
        end_line=2,
        chunk="CHANGED",
    )
    assert "campaign/doc.md" in result
    assert (vault / "campaign" / "doc.md").read_text().splitlines()[2] == "CHANGED"


def test_vault_file_tools_still_blocks_outside_absolute(tmp_path):
    vault = tmp_path / "vault"
    vault.mkdir()
    outside = Path("/tmp") / "foundry_outside" / "secret.md"
    outside.parent.mkdir(parents=True, exist_ok=True)
    outside.write_text("secret")

    ft = VaultFileTools(base_dir=vault)
    assert "secret" not in ft.read_file(str(outside))
