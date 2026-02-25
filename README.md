# 🤖 Local RAG AI - Your Private Manual Consultant

[![Ollama](https://img.shields.io/badge/LLM-Ollama-blue.svg)](https://ollama.com/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green.svg)](https://www.python.org/)
[![UI](https://img.shields.io/badge/UI-Glassmorphism-purple.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A high-performance, **100% private**, and local Retrieval-Augmented Generation (RAG) system. Chat with your technical manuals (PDFs) without an internet connection using state-of-the-art open-source models.

![Project Preview](https://via.placeholder.com/800x450.png?text=Local+RAG+Interface+Preview)

## ✨ Features

- 🔒 **Total Privacy**: Everything runs on your machine. No data leaves your network.
- ⚡ **AI Models**: Powered by **Llama 3.2** (Intelligence) and **Nomic Embed Text** (Context).
- 🎨 **Premium UI**: Modern glassmorphism interface with dark mode and smooth animations.
- 📂 **Multi-PDF Support**: Upload and index multiple manuals simultaneously.
- 📍 **Source Transparency**: Precise citations of where information was found in the documents.
- 🏗️ **Smart Chunking**: Advanced text splitting for accurate information retrieval.

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, Tailwind CSS, Lucide Icons
- **RAG Framework**: LangChain
- **Vector Database**: ChromaDB
- **LLM Engine**: Ollama

## 🚀 Getting Started

### 1. Prerequisites
- Install [Ollama](https://ollama.com/)
- Download required models:
  ```bash
  ollama pull llama3.2
  ollama pull nomic-embed-text
  ```

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/nardet30/sistema-rag-local.git
cd sistema-rag-local
pip install -r requirements.txt
```

### 3. Usage
1. Place your PDF manuals in the `data/` folder.
2. Run the application:
   ```bash
   python app.py
   ```
3. Open your browser at [http://localhost:8000](http://localhost:8000).

## 📂 Project Structure

```text
├── app.py             # FastAPI Server & API Endpoints
├── src/
│   ├── rag_engine.py  # Core Logic: Embedding, Retrieval & LLM Chain
│   └── config.py      # System Configurations
├── templates/
│   └── index.html     # Premium Web Interface
├── data/              # Put your PDFs here
└── vector_db_local/   # Persistent local vector storage
```

## 🌐 GitHub Pages (Preview)
Check out the [Landing Page](https://nardet30.github.io/sistema-rag-local/) to see the interface design and features.

## 🤝 Contributing
Feel free to open issues or submit pull requests. All contributions that improve speed or UX are welcome!

---
Developed with ❤️ by [nardet](https://github.com/nardet30)
