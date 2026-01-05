import asyncio
from importlib.metadata import version

from mcp.server import Server


async def test_installation():
    """MCPインストールの検証"""

    print("MCPインストールの検証を開始します...")

    mcp_version = version("mcp")
    print(f"☑️ MCP version: {mcp_version}")

    try:
        server = Server("mcp-server-test")
        print(f"☑️ MCPサーバーが正常に起動しました: {server.name}")
    except Exception as e:
        print(f"❌ MCPサーバーの起動に失敗しました: {e}")
        return


if __name__ == "__main__":
    asyncio.run(test_installation())
