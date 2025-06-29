# config.py

import os
from pathlib import Path

class Config:
    #  Keys 
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    EMBEDDING_MODEL = "llama-embed-8b"  
    CHAT_MODEL = "llama3-8b-8192"  

    # --- Chunking Settings ---
    CHUNK_SIZE = 500  # Characters per chunk
    CHUNK_OVERLAP = 50  # Overlap between chunks for context preservation

    # --- FAISS Settings ---
    INDEX_PATH = Path("vector_store/index.faiss")
    METADATA_PATH = Path("vector_store/metadata.pkl")

    # --- Retrieval Settings ---
    TOP_K = 5  # Number of chunks to retrieve for answering a question

    # --- Misc ---
    LOGGING = True
    DEBUG = False

# Optional: Create output directories if they don't exist
Path(Config.INDEX_PATH).parent.mkdir(parents=True, exist_ok=True)
