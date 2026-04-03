'''
Author: Armand Meijers
Date: 02/04/2026
Description: takes in text and embedds it in a vector DB
'''

import os, json, faiss
from sentence_transformers import SentenceTransformer
import numpy as np

def embedding_text(datafile_path):
    """
    Takes metadata JSON path (with chunks), extracts all text, and embeds it into a vector DB.

    Args:
        datafile_path (str):    path to chunk metadata JSON (e.g., data/processed/metadata/xxx.json) 
    """

    model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    dimension = 1024
    index = faiss.IndexFlatL2(dimension)

    with open(datafile_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, batch_size=16, show_progress_bar=True)
    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)
    
    faiss.write_index(index, "data/vector_DB/index.faiss")

