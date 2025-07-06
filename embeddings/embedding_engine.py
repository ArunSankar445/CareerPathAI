from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def get_embedding(text):
    """
    Converts input text into embedding vector.
    """
    return model.encode(text)
