from mcp.server.fastmcp import FastMCP
from markitdown import MarkItDown


mcp = FastMCP(
    name="Markitdown Wrap MCP Server",
    description="MCP server for Markitdown conversion service",
    version="0.1.0",
    author="Oya-Tomo",
)


@mcp.tool(name="convert_file_to_markdown")
async def convert_file_to_markdown(file_path: str) -> str:
    """
    Convert a file to Markdown format.

    Args:
        file_path: Path to the file to convert

    Returns:
        str: Converted Markdown text
    """
    try:
        # Initialize MarkItDown converter
        md = MarkItDown()

        # Convert file to markdown
        result = md.convert(file_path)

        # Return the converted text
        return result.text_content

    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error converting file to markdown: {str(e)}")


if __name__ == "__main__":
    mcp.run()
