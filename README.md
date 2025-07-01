# Markitdown Wrap MCP

## Dependencies

- uv: python package manager

## Usage

Add the following configuration to .vscode/settings.json .

```json
{
  "mcp": {
    "servers": {
      "markitdown-wrap-mcp": {
        "type": "stdio",
        "cwd": "/path/to/markitdown-wrap-mcp",
        "command": "uv",
        "args": ["run", "python", "src/server.py"]
      }
    }
  }
}
```

## tools

- convert_file_to_markdown: PDF to Markdown Text
