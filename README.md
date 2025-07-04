# 🩺 Medical Assistant — RAG App with FastAPI, FAISS, Qwen & Cohere

This project is a **Retrieval-Augmented Generation (RAG)** pipeline for answering medical domain questions.  
It combines:

- **Qwen Embedding model** (open source)
- **FAISS** for fast vector search
- **Cohere** (Command R+) as your free hosted LLM

🚀 **Deployed on [Render](https://render.com/)** with a free tier — no GPUs required!

---

## 📌 Features

✅ Ingest a medical Q&A corpus  
✅ Generate embeddings using Qwen  
✅ Index vectors with FAISS  
✅ Retrieve top-k context for a query  
✅ Generate grounded answers using Cohere’s LLM  
✅ Easily swap embedding or LLM models

---

## 🗂️ Project Structure

.
├── app/
│ ├── main.py # FastAPI entrypoint
│ ├── ingestion.py # Loads and embeds corpus
│ ├── embeddings.py # Qwen embedding model
│ ├── faiss_index.py # FAISS index handling
│ ├── schemas.py # Pydantic models for requests
│ ├── llm.py # Cohere LLM integration
│ └── data.json # Sample medical Q&A
├── .env # API keys & config
├── requirements.txt
├── README.md

yaml
Copy
Edit

---

## ⚡ Quickstart

### 1️⃣ Clone the repo

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
2️⃣ Create a virtual environment
bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
3️⃣ Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file:

env
Copy
Edit
COHERE_API_KEY=your_cohere_api_key
LLM_PROVIDER=cohere
🗃️ Ingest your corpus
Place your data.json in the app/ directory.

On startup, the app will embed your data and build/load the FAISS index.

🚀 Run locally
bash
Copy
Edit
uvicorn app.main:app --reload
Try the /ask endpoint:

json
Copy
Edit
POST /ask

{
  "question": "Who is at risk for LCM?",
  "top_k": 3
}
The API will:

Embed your query

Retrieve top-k relevant chunks

Call Cohere’s LLM with your context

Return a grounded answer!

🌐 Deploy to Render (FREE)
Push your repo to GitHub

Create a new Render Web Service

Build Command: pip install -r requirements.txt

Start Command: uvicorn app.main:app --host 0.0.0.0 --port 10000

Add your environment variables (COHERE_API_KEY, LLM_PROVIDER)

🚀 Done!
```
