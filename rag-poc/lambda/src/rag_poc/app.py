import json
from rag_service import ingest_markdown_to_vector_store, search_and_answer


def lambda_handler(event, context):
    path = event.get("path", "")
    body = json.loads(event.get("body") or "{}")

    if path.endswith("/ingest"):
        text = body["text"]
        doc_path = body.get("path", "unknown.md")
        result = ingest_markdown_to_vector_store(text, doc_path)
        return _res(200, result)

    if path.endswith("/search"):
        query = body["query"]
        top_k = int(body.get("top_k", 5))
        result = search_and_answer(query, top_k=top_k)
        return _res(200, result)

    return _res(404, {"error": "not found"})


def _res(status, body):
    return {
        "statusCode": status,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body, ensure_ascii=False),
    }
