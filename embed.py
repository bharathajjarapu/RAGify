from fastembed import TextEmbedding
import numpy as np
import faiss

class EmbeddingHandler:
    def __init__(self, dimension=384):
        self.embedding_model = TextEmbedding()
        self.dimension = dimension
        self.index = self.create_index()

    def create_index(self):
        """Create a FAISS index"""
        return faiss.IndexFlatL2(self.dimension)

    def embed_texts(self, texts):
        """Create embeddings for a list of texts"""
        embeddings = list(self.embedding_model.embed(texts))
        return np.array(embeddings).astype('float32')

    def add_to_index(self, embeddings):
        """Add embeddings to FAISS index"""
        self.index.add(embeddings)

    def search_similar(self, query, k=3):
        """Search for similar embeddings"""
        query_embedding = list(self.embedding_model.embed([query]))[0].astype('float32')
        D, I = self.index.search(query_embedding.reshape(1, -1), k)
        return I[0] 