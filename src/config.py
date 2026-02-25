class Config:
    VECTOR_DB_PATH = "vector_db_local"
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 150
    # Modelo Llama 3.2 (Más fiable y ligero, 2GB)
    LLM_MODEL = "llama3.2"
    EMBEDDING_MODEL = "nomic-embed-text"
    OLLAMA_BASE_URL = "http://localhost:11434"
