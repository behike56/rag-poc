# server.py
import os
import httpx
from mcp.server import Server
from mcp.types import Tool

API_BASE = os.environ.get(
    "RAG_API_BASE",
    "https://your-api-gw.execute-api.ap-northeast-1.amazonaws.com/prod",
)

server = Server("aws-rag")


@server.tool()
async def rag_ingest_markdown(path: str, text: str) -> dict:
    """
    Markdown を RAG に登録するツール
    """
    url = f"{API_BASE}/ingest"
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, json={"path": path, "text": text})
        r.raise_for_status()
        return r.json()


@server.tool()
async def rag_search_and_answer(query: str, top_k: int = 5) -> dict:
    """
    Markdown RAG で検索して回答＋ソースを返すツール
    """
    url = f"{API_BASE}/search"
    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(url, json={"query": query, "top_k": top_k})
        r.raise_for_status()
        return r.json()


if __name__ == "__main__":
    # STDIO モードで起動（Cursor から呼ばれやすい）
    server.run_stdio()
