import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient

load_dotenv()

async def main():

    # Configure Tavily's remote MCP server
    client = MultiServerMCPClient({
        "tavily": {
            "transport": "http",
            "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.environ['TAVILY_API_KEY']}"
        }
    })

    # Discover tools
    tools = await client.get_tools()

    print("\nAvailable MCP Tools:")
    for tool in tools:
        print(f"- {tool.name}: {tool.description[:100]}")

    # Find the search tool
    search_tool = next(
        tool for tool in tools
        if tool.name in ("tavily_search", "tavily-search")
    )

    # Test a real web search
    result = await search_tool.ainvoke({
        "query": "What is Zaph Body Care"
    })

    print("\nSearch Results:")
    print(result)

if __name__ == "__main__":
    asyncio.run(main())