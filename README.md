# Demo MCP server

A small Python MCP server that Claude Desktop can use to save notes and add
numbers. It uses the MCP Python SDK 2.x.

## Requirements

- Python 3.11 or newer
- [uv](https://docs.astral.sh/uv/)
- Claude Desktop, if you want to use the server from Claude

## Run locally

From the project directory:

```sh
uv sync
uv run mcp run main.py
```

The command starts an MCP server over standard input and output; it is intended
to be launched by an MCP client rather than used as an interactive prompt.

## Connect Claude Desktop

In Claude Desktop, open **Settings > Desktop app > Edit config** and add a
`main` entry to `mcpServers`. Replace the paths below with the output of
`which uv` and the absolute path to your copy of this project:

```json
{
  "mcpServers": {
    "main": {
      "command": "/absolute/path/to/uv",
      "args": [
        "--directory",
        "/absolute/path/to/LLM-Apps",
        "run",
        "--locked",
        "mcp",
        "run",
        "main.py"
      ]
    }
  }
}
```

If you already have other server entries or settings, add only the `main`
entry inside the existing `mcpServers` object rather than replacing the file.
Quit and reopen Claude Desktop after changing the configuration or server code.

## Capabilities

- `add_note(message)`: appends a note to `notes.txt` next to `main.py`.
  When the file is first created, the current code writes `HOLAA` before the
  first note, without a newline.
- `add(a, b)`: returns the sum of two integers.
- `greeting://{name}`: returns a greeting for the given name.

Notes and the personal Claude Desktop configuration are ignored by Git. If a
note fails to save, check the server logs in Claude Desktop and confirm that
the server has permission to write to the project directory.