# 🤖 Local RAG AI - Tu Consultor Privado de Manuales

[![Ollama](https://img.shields.io/badge/LLM-Ollama-blue.svg)](https://ollama.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![Interfaz](https://img.shields.io/badge/Interfaz-Glassmorphism-purple.svg)](#)
[![Licencia: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Un sistema de Generación Aumentada por Recuperación (RAG) de alto rendimiento, **100% privado** y local. Chatea con tus manuales técnicos (PDFs) sin necesidad de conexión a internet, utilizando modelos de código abierto de última generación.

![Previsualización del Proyecto](https://via.placeholder.com/800x450.png?text=Interfaz+RAG+Local+Preview)

## ✨ Características

- 🔒 **Privacidad Total**: Todo se ejecuta en tu máquina. Ningún dato sale de tu red local.
- ⚡ **Modelos IA**: Potenciado por **Llama 3.2** (Inteligencia) y **Nomic Embed Text** (Contexto).
- 🎨 **Interfaz Premium**: Diseño moderno con efecto "Glassmorphism", modo oscuro y animaciones fluidas.
- 📂 **Gestión de Documentos**: Sube y re-indexa múltiples manuales PDF directamente desde la web.
- 📍 **Transparencia en Fuentes**: Citas precisas de los documentos y páginas donde se encontró la información.
- 🏗️ **Fragmentación Inteligente**: Procesamiento avanzado de texto para una recuperación de información exacta.

## 🛠️ Tecnologías

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, Tailwind CSS, Lucide Icons
- **Framework RAG**: LangChain
- **Base de Datos Vectorial**: ChromaDB
- **Motor LLM**: Ollama

## 🚀 Primeros Pasos

### 1. Requisitos previos
- Instala [Ollama](https://ollama.com/)
- Descarga los modelos necesarios:
  ```bash
  ollama pull llama3.2
  ollama pull nomic-embed-text
  ```

### 2. Instalación
Clona el repositorio e instala las dependencias:
```bash
git clone https://github.com/nardet30/sistema-rag-local.git
cd sistema-rag-local
pip install -r requirements.txt
```

### 3. Uso
1. Inicia el servidor:
   ```bash
   python app.py
   ```
2. Abre tu navegador en [http://localhost:8000](http://localhost:8000).
3. Sube tus manuales PDF a través de la interfaz y pulsa el botón de **Re-indexar**.

## 📂 Estructura del Proyecto

```text
├── app.py             # Servidor FastAPI y Endpoints de la API
├── src/
│   ├── rag_engine.py  # Lógica Central: Embeddings, Recuperación y Cadena LLM
│   └── config.py      # Configuraciones del Sistema
├── templates/
│   └── index.html     # Interfaz Web Premium
├── data/              # Carpeta de almacenamiento de tus PDFs
└── vector_db_local/   # Almacenamiento persistente de la base de datos vectorial
```

## 🌐 GitHub Pages (Presentación)
Visita nuestra [Landing Page](https://nardet30.github.io/sistema-rag-local/) para ver el diseño de la interfaz y sus capacidades.

## 🤝 Contribuciones
Siéntete libre de abrir issues o enviar pull requests. ¡Cualquier mejora en velocidad o experiencia de usuario es bienvenida!

---
Desarrollado con ❤️ por [nardet](https://github.com/nardet30)
