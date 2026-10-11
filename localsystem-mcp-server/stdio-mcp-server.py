from fastmcp import FastMCP

mcp = FastMCP("My-STDIO-Server")

# Tool 1 (FastMCP uses docstrings and type hints for JSON Schema)
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Use this tool to add two integers numbers together."""
    return a + b

# Tool 2
@mcp.tool()
def get_user_greeting(name: str) -> str:
    """Use this tool to generate a greeting message for a user."""
    return f"Hello, {name}! Welcome to the MCP world."

# Tool 3
@mcp.tool()
def welcome_msg() -> str:
    """Use this tool to generate a welcome message."""
    return "Welcome to My FastMCP STDIO server!"


# 4. Run server on STDIO transport
if __name__ == "__main__":
    mcp.run(transport="stdio")
