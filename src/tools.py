from agno.tools.coding import CodingTools
from agno.tools.file import FileTools
from agno.tools.local_file_system import LocalFileSystemTools
from agno.tools.workspace import Workspace

from config import VAULT_DIR


def build_read_tools() -> FileTools:
    return FileTools(
        base_dir=VAULT_DIR,
        enable_save_file=False,
        enable_read_file=True,
        enable_delete_file=False,
        enable_list_files=True,
        enable_search_files=True,
        enable_read_file_chunk=True,
        enable_replace_file_chunk=False,
        enable_search_content=True,
        expose_base_directory=False,
    )


def build_editor_tools() -> FileTools:
    return FileTools(
        base_dir=VAULT_DIR,
        enable_save_file=True,
        enable_read_file=True,
        enable_delete_file=False,
        enable_list_files=True,
        enable_search_files=True,
        enable_read_file_chunk=True,
        enable_replace_file_chunk=True,
        enable_search_content=True,
        expose_base_directory=False,
    )


def build_coding_tools():
    return CodingTools(
        base_dir=VAULT_DIR,
        enable_read_file=True,
        enable_edit_file=True,
        enable_write_file=True,
        enable_run_shell=True,
        enable_grep=True,
        enable_find=True,
        enable_ls=True,
        allowed_commands=[
            "cat",
            "head",
            "tail",
            "wc",
            "ls",
            "find",
            "grep",
            "mkdir",
            "rm",
            "mv",
            "cp",
            "touch",
            "echo",
            "printf",
            "diff",
            "sort",
            "uniq",
            "tr",
            "cut",
        ],
        requires_confirmation_tools=["write_file", "edit_file", "run_shell"],
    )


def build_workspace_tools(confirm: bool = False) -> Workspace:
    return Workspace(
        root=str(VAULT_DIR),
        confirm=["write", "edit", "move", "delete", "shell"] if confirm else None,
    )


def build_local_file_system_tools():
    return LocalFileSystemTools(
        target_directory=str(VAULT_DIR),
        default_extension="md",
        external_execution_required_tools=["write_file"],
    )
