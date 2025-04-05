from fastapi import FastAPI, Query
from typing import Dict

app = FastAPI()

# Placeholder for your RAG logic
def get_rag_response(query: str) -> str:
    # Here you will connect your product catalog logic
    return f"You asked: '{query}'. Here's a placeholder RAG response."

@app.get("/query")
def query_endpoint(text: str = Query(..., description="Enter your question here")) -> Dict:
    response = get_rag_response(text)
    return {"query": text, "response": response}
