from fastmcp import FastMCP

# Initialize the FastMCP server instance
mcp = FastMCP("Streamable-HTTP-Server")

# Register your tools using decorators
@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Use this tool to add two numbers together."""
    return a + b

@mcp.tool()
def get_user_greeting(name: str) -> str:
    """Use this tool to generate a greeting message for a remote user."""
    return f"Hello, {name}! Welcome to the remote Streamable HTTP MCP server."

@mcp.tool()
def welcome_msg() -> str:
    """Use this tool to generate a welcome message."""
    return "Welcome to My Streamable HTTP MCP server!"

# Entry point: Run using streamable-http transport
if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8050)
