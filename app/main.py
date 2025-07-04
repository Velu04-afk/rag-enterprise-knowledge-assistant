from fastapi import FastAPI
from app.ingestion import ingest_corpus
from app.embeddings import embedding_model
from app.faiss_index import faiss_index
from app.schemas import QueryRequest
from dotenv import load_dotenv
import os

app = FastAPI(title="Medical Assistant")

load_dotenv()


@app.on_event("startup")
async def startup():
    try:
        faiss_index.load("medical_index.faiss", "medical_docs.json")
        print("✅ FAISS index & docs loaded from disk")
    except Exception as e:
        ingest_corpus("datasets/data.json")


@app.post("/ask")
async def ask_question(query: QueryRequest):
    query_vector = embedding_model.embed(query.question)

    results = faiss_index.search(query_vector, k=3)

    # Simple return
    return {"question": query.question, "top_k": query.top_k, "results": results}
