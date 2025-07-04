from app.faiss_index import FaissIndex, faiss_index
import json


def ingest_corpus(file_path: str):
    global faiss_index

    # 1️⃣ Load your data
    with open(file_path) as f:
        data = json.load(f)

    print(f"✅ Loaded {len(data)} records")

    # 2️⃣ Get embedding dimension
    from app.embeddings import embedding_model
    test_vector = embedding_model.embed("test")
    dim = len(test_vector)
    print(f"✅ Embedding dimension: {dim}")

    # 3️⃣ Create new index with correct dim
    faiss_index = FaissIndex(dim)

    # 4️⃣ Add vectors
    for idx, record in enumerate(data):
        combined_text = f"Q: {record['question']} A: {record['answer']}"
        vector = embedding_model.embed(combined_text)

        doc = {
            "id": idx,
            "text": combined_text,
            "metadata": {
                "type": record.get("type", "unknown")
            }
        }

        faiss_index.add(vector, doc)

    print(f"✅ Added {len(faiss_index.documents)} docs")

    # 5️⃣ SAVE index & docs to disk!
    faiss_index.save("medical_index.faiss", "medical_docs.json")
    print("✅ Saved FAISS index & metadata to disk.")
