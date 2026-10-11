import asyncio
from langchain_mcp_adapters import client, tools
from langchain_mcp_adapters.client import MultiServerMCPClient

# Define the server configuration
MCP_CONFIG = {
    "stdio_server": {
        "transport": "stdio",
        "command": "uv",
        "args": ["run", "localsystem-mcp-server/stdio-mcp-server.py"], 
    }
}

async def main():
    # Instantiate the client with configuration
    client = MultiServerMCPClient(MCP_CONFIG)   
    tools = await client.get_tools()
    
    print("\n--- Discovered Tools ---")
    for t in tools:
            print(f"Tool Name: {t.name} | Description(DOC STRINGS): {t.description}")

# Correctly run the async main function
if __name__ == "__main__":
    asyncio.run(main())
