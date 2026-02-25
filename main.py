import os
import sys
from src.rag_engine import RAGEngine
from src.config import Config

def main():
    print("=== Sistema RAG Local con Ollama ===")
    config = Config()
    engine = RAGEngine()

    # 1. Verificar si la carpeta data existe y tiene PDFs
    if not os.path.exists("data"):
        os.makedirs("data")
        print("Error: La carpeta 'data' no existía. Se ha creado. Pon tus PDFs dentro y reinicia.")
        return

    pdfs = [f for f in os.listdir("data") if f.endswith(".pdf")]
    if not pdfs:
        print("Error: No se han encontrado archivos PDF en la carpeta 'data'.")
        print("Por favor, copia tus manuales a la carpeta 'data' y reinicia el programa.")
        return
    
    print(f"Archivos encontrados en 'data': {pdfs}")

    # 2. Forzar ingesta si la base de datos no existe
    if not os.path.exists(config.VECTOR_DB_PATH):
        print(f"Base de datos no encontrada. Iniciando procesamiento de {len(pdfs)} documentos...")
        engine.ingest_documents("data")
    else:
        print(f"Base de datos cargada desde: {config.VECTOR_DB_PATH}")
        print("Si has añadido PDFs nuevos, borra la carpeta 'vector_db_local' para que el sistema los lea.")

    # 3. Bucle de consultas
    while True:
        query_text = input("\nPregunta (o 'salir' para terminar): ")
        
        if query_text.lower() in ['salir', 'exit', 'quit']:
            break

        if not query_text.strip():
            continue

        try:
            print("Pensando...")
            result = engine.query(query_text)
            
            print("\n--- RESPUESTA ---")
            print(result["answer"])
            
            print("\n--- FUENTES ---")
            if result["source_documents"]:
                for doc in result["source_documents"]:
                    source = doc.metadata.get("source", "Desconocido")
                    page = doc.metadata.get("page", "?")
                    print(f"- {os.path.basename(source)} (Página {page})")
            else:
                print("No se encontraron fragmentos relevantes en los documentos.")
                
        except Exception as e:
            print(f"Error al procesar la consulta: {e}")

if __name__ == "__main__":
    main()
