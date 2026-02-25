import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from src.rag_engine import RAGEngine
from src.config import Config
import uvicorn
import shutil
from fastapi import FastAPI, Request, Form, File, UploadFile


app = FastAPI(title="RAG Local Ollama UI")

# Configuración de directorios
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

if not os.path.exists(TEMPLATES_DIR):
    os.makedirs(TEMPLATES_DIR)

templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Inicializar motor RAG
engine = RAGEngine()
config = Config()

# Asegurar que la DB esté lista al arrancar
if not os.path.exists(config.VECTOR_DB_PATH):
    print("Base de datos no encontrada. Procesando documentos...")
    if os.path.exists("data"):
        engine.ingest_documents("data")
    else:
        print("Error: Carpeta 'data' no encontrada.")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    pdfs = []
    if os.path.exists("data"):
        pdfs = [f for f in os.listdir("data") if f.endswith(".pdf")]
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "pdfs": pdfs,
        "db_status": "Lista" if os.path.exists(config.VECTOR_DB_PATH) else "No creada"
    })

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".pdf"):
            return {"error": "Solo se permiten archivos PDF."}
        
        data_dir = "data"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
            
        file_path = os.path.join(data_dir, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        return {"message": f"Archivo {file.filename} subido correctamente. Pulsa Re-indexar para procesarlo."}
    except Exception as e:
        return {"error": str(e)}

@app.post("/reindex")
async def reindex_documents():
    try:
        if os.path.exists(config.VECTOR_DB_PATH):
            import shutil
            # En Windows a veces da error si hay archivos abiertos, pero Chroma suele manejarlo o cerramos el motor
            # Para simplificar borramos y reiniciamos el motor
            engine.vector_store = None
            shutil.rmtree(config.VECTOR_DB_PATH)
            
        engine.ingest_documents("data")
        return {"message": "Base de datos actualizada correctamente con los nuevos documentos."}
    except Exception as e:
        return {"error": str(e)}

@app.post("/ask")

async def ask_question(question: str = Form(...)):
    try:
        result = engine.query(question)
        
        sources = []
        if result["source_documents"]:
            for doc in result["source_documents"]:
                sources.append({
                    "name": os.path.basename(doc.metadata.get("source", "Desconocido")),
                    "page": doc.metadata.get("page", "?")
                })
        
        return {
            "answer": result["answer"],
            "sources": sources
        }
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
