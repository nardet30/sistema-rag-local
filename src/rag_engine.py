import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.config import Config

class RAGEngine:
    def __init__(self):
        self.config = Config()
        # Embeddings locales
        self.embeddings = OllamaEmbeddings(
            model=self.config.EMBEDDING_MODEL,
            base_url=self.config.OLLAMA_BASE_URL
        )
        # LLM local
        self.llm = ChatOllama(
            model=self.config.LLM_MODEL,
            temperature=0,
            base_url=self.config.OLLAMA_BASE_URL
        )
        self.vector_store = None

    def ingest_documents(self, directory_path: str):
        print(f"--- Iniciando Ingesta Local (Ollama) ---")
        loader = DirectoryLoader(directory_path, glob="./*.pdf", loader_cls=PyPDFLoader)
        docs = loader.load()
        
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.config.CHUNK_SIZE,
            chunk_overlap=self.config.CHUNK_OVERLAP
        )
        chunks = text_splitter.split_documents(docs)
        
        print(f"Procesando {len(chunks)} fragmentos con el modelo {self.config.EMBEDDING_MODEL}...")
        
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=self.embeddings,
            persist_directory=self.config.VECTOR_DB_PATH
        )
        print("Éxito: Base de datos vectorial local creada.")

    def query(self, user_input: str):
        if not self.vector_store:
            self.vector_store = Chroma(
                persist_directory=self.config.VECTOR_DB_PATH,
                embedding_function=self.embeddings
            )

        retriever = self.vector_store.as_retriever(search_kwargs={"k": 4})

        template = """Responde en ESPAÑOL la pregunta basándote solo en el contexto:
        contexto: {context}

        pregunta: {question}
        
        Si no está en el contexto, di que no lo sabes. Menciona el documento fuente.
        """
        prompt = ChatPromptTemplate.from_template(template)

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        context_docs = retriever.invoke(user_input)
        
        chain = (
            {"context": lambda x: format_docs(context_docs), "question": RunnablePassthrough()}
            | prompt
            | self.llm
            | StrOutputParser()
        )
        
        response = chain.invoke(user_input)
        
        return {
            "answer": response,
            "source_documents": context_docs
        }
