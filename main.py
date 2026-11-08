import os

from mcp.server.mcpserver import MCPServer
from pathlib import Path

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")
mcp = MCPServer("Demo")


def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("HOLAA")


@mcp.tool()
def add_note(message:str) ->str :
    """_summary_
    Append a new note to the sticky note file
    Args:
        message (str):The note to be added

    Returns:
        str: Confirmation message saying the note is added
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
    return "Notes saved !"


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"

def main():
    print("Hello from llm-apps!")


if __name__ == "__main__":
    main()
