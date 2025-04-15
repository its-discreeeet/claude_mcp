# server.py
from mcp.server.fastmcp import FastMCP
import os

# MCP server creation
mcp = FastMCP("basic_mcp")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")
def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

#tools
@mcp.tool()
def add_note(note : str) -> str:
    """
    Add a note to the notes file

    Args : note(str) : The note to add

    Returns : str : a message stating the note was added followed by the note itself
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    return f"Added note : {note}"

@mcp.tool()
def get_notes() -> str:
    """
    Fetches the notes from the notes.txt file
    
    Args : None
    
    Returns : str : The contents of the notes.txt file
    """
    ensure_file()

    with open("NOTES_FILE", "r") as f:
        notes = f.read().strip()
    return notes or "No notes found."

#resources
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.resource("notes://latest")
def get_latest_note() -> str:
    """
    Get the latest note from the notes file

    Args : None

    Returns : str : The latest note or a message stating no notes were found
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.readlines()
    return notes[-1].strip() if notes else "No notes found."

#prompt
@mcp.prompt()
def note_summary_prompt() -> str:
    """
    A prompt to summarize the notes in the notes file

    Args : None

    Returns : str : A summary of the notes
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        notes = f.read().strip()
    if not notes:
        return "No notes found."
   
    return f"Summarize the content of notes:{notes}"
