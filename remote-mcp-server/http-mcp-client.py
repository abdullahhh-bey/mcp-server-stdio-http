import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


# Configuration dictionary for remote HTTP servers
MCP_CONFIG = {
    "remote_http_server": {
        "transport": "streamable-http",
        "url": "http://localhost:8050/mcp",
    }
}


async def main():
    # Instantiate the multi-server client
    client = MultiServerMCPClient(MCP_CONFIG)
    
    # Discover available tools over the HTTP endpoint
    tools = await client.get_tools()
    
    print("\n--- Discovered Tools from Remote HTTP Server ---")
    for t in tools:
        print(f"Tool Name: {t.name} | Description: {t.description}")

if __name__ == "__main__":
    asyncio.run(main())
