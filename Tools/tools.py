import pathlib
from langchain_core.tools import tool

# Project root directory where all files will be stored/managed
PROJECT_ROOT = pathlib.Path.cwd() / "generated_project"

def safe_path_for_project(path: str) -> pathlib.Path:
    """
    Resolve a given path inside PROJECT_ROOT safely.

    Ensures that the resolved path stays within PROJECT_ROOT 
    to prevent directory traversal attacks or writing outside
    the project directory.
    """
    root = PROJECT_ROOT.resolve()
    p = (root / path).resolve()

    if root not in p.parents and root != p.parent and root != p:
        raise ValueError(f"Attempt to access outside project root: {p}")

    return p


def write_file(path: str, content: str) -> str:
    """
    Writes the provided content to the specified file path.
    :param path: The filepath to write to.
    :param content: The full content to write to the file.
    :return: A success or error message string.
    """
    p = safe_path_for_project(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")
    return f"WROTE: {p}"


def read_file(path: str) -> str:
    """
    Read and return the contents of a file inside the project root.

    Returns an empty string if the file does not exist.
    """
    p = safe_path_for_project(path)
    return p.read_text(encoding="utf-8") if p.exists() else ""


def get_current_directory() -> str:
    """
    Return the absolute path of the project root directory.
    """
    return str(PROJECT_ROOT.resolve())


def list_all_files(directory: str = ".") -> str:
    """
    Lists the files and directories in a specified path.
    :param directory: The path of the directory to list (defaults to ".").
    :return: A string listing the files and directories found.
    """
    p = safe_path_for_project(directory)
    if not p.is_dir():
        return f"ERROR: {p} is not a directory"

    files = [str(f.relative_to(PROJECT_ROOT)) for f in p.rglob("*") if f.is_file()]
    return "\n".join(files) if files else "No files found."


def init_project_root() -> str:
    """
    Initialize the project root directory if it doesn't exist.
    Returns the absolute path to the project root.
    """
    PROJECT_ROOT.mkdir(parents=True, exist_ok=True)
    return str(PROJECT_ROOT.resolve())
