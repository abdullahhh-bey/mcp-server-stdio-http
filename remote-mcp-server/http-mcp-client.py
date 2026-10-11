import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


# Configuration dictionary for remote HTTP servers -> It's the USB-C PORT 
MCP_CONFIG = {
    "remote_http_server": {
        "transport": "streamable-http",
        "url": "http://localhost:8050/mcp",
    },
    "stdio_server": {
            "transport": "stdio",
            "command": "uv",
            "args": ["run", "localsystem-mcp-server/stdio-mcp-server.py"], 
        }
}


async def main():
    # Instantiate the multi-server client
    client = MultiServerMCPClient(MCP_CONFIG)
    
    # Discover available tools over the HTTP endpoint
    tools = await client.get_tools()
    
    print("\n--- Discovered Tools from both MCP Servers ---")
    for t in tools:
        print(f"Tool Name: {t.name} | Description: {t.description}")

if __name__ == "__main__":
    asyncio.run(main())
