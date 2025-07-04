import faiss
import json
import numpy as np


class FaissIndex:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatL2(dim)
        self.documents = []

    def add(self, vector, doc):
        vector_np = np.array([vector]).astype('float32')
        self.index.add(vector_np)
        self.documents.append(doc)

    def save(self, index_file="medical_index.faiss", docs_file="medical_docs.json"):
        faiss.write_index(self.index, index_file)
        with open(docs_file, "w") as f:
            json.dump(self.documents, f)

    def load(self, index_file="medical_index.faiss", docs_file="medical_docs.json"):
        self.index = faiss.read_index(index_file)
        with open(docs_file) as f:
            self.documents = json.load(f)

    def search(self, vector, k=3):
        vector_np = np.array([vector]).astype('float32')
        distances, indices = self.index.search(vector_np, k)
        results = []
        for idx in indices[0]:
            if idx < len(self.documents):
                results.append(self.documents[idx])
        return results


# Global
faiss_index = FaissIndex(dim=1024)  # or your dim
