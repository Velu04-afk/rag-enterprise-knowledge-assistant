from transformers import AutoTokenizer, AutoModel
import torch


class EmbeddingModel:
    def __init__(self, model_name="Qwen/Qwen3-Embedding-0.6B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def embed(self, text: str) -> list[float]:
        inputs = self.tokenizer(text, return_tensors="pt",
                                truncation=True, padding=True)
        with torch.no_grad():
            embeddings = self.model(**inputs)
        # Pool to a single vector
        vector = embeddings.last_hidden_state.mean(dim=1).squeeze().tolist()
        return vector


embedding_model = EmbeddingModel()
