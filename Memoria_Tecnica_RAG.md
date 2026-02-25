# Memoria de Desarrollo: Sistema RAG Local con Ollama

**Estudiante:** [Tu Nombre]
**Proyecto:** Consultor Técnico de Manuales PDF (Privacidad Garantizada)
**Fecha:** 25 de Febrero de 2026

---

## 1. Resumen del Proyecto
El objetivo ha sido desarrollar una aplicación web local que permita a los usuarios realizar consultas en lenguaje natural sobre manuales técnicos en formato PDF. La solución garantiza la privacidad total al ejecutar tanto el modelo de lenguaje (LLM) como la base de datos de conocimientos de forma local en el ordenador del usuario utilizando **Ollama**.

## 2. Cronología del Desarrollo

### Fase 1: Configuración del Motor RAG
*   **Tarea:** Implementar la lógica de Recuperación Aumentada por Generación (RAG).
*   **Tecnologías:** LangChain, ChromaDB y Ollama.
*   **Hitos:**
    *   Configuración del modelo de inteligencia: **Llama 3.2**.
    *   Configuración del modelo de contexto (Embeddings): **Nomic Embed Text**.
    *   Implementación de la fragmentación de documentos (Chunking) para optimizar la búsqueda.

### Fase 2: Creación de la Interfaz Web y Servidor
*   **Tarea:** Desarrollar un backend robusto y una interfaz de usuario atractiva.
*   **Tecnologías:** FastAPI, Jinja2 y Tailwind CSS.
*   **Hitos:**
    *   Creación de un servidor FastAPI para gestionar las consultas.
    *   Diseño de una interfaz moderna con estilo *Glassmorphism* y animaciones fluidas para una experiencia de usuario "premium".

### Fase 3: Gestión de Archivos y Mejoras de UX
*   **Tarea:** Permitir la interacción dinámica con los documentos desde la web.
*   **Hitos:**
    *   Implementación de carga de archivos PDF desde el navegador.
    *   Añadido sistema de "Re-indexación" para actualizar la base de conocimientos sin reiniciar el programa.
    *   Inclusión de citas exactas (documento y página) en las respuestas de la IA.

### Fase 4: Preparación para Distribución (GitHub)
*   **Tarea:** Documentar y organizar el código para su publicación.
*   **Hitos:**
    *   Creación de un README profesional en español.
    *   Configuración de GitHub Pages para una landing page de presentación.
    *   Gestión de versiones con Git.

---

## 3. Desafíos y Soluciones (Log de Errores)

| Error / Problema | Causa Identificada | Solución Aplicada |
| :--- | :--- | :--- |
| **Conexión rechazada con Ollama** | El servicio de Ollama no estaba iniciado o los modelos no estaban descargados. | Se creó un script de verificación (`test_ollama.py`) y se aseguró que el servicio estuviera activo antes de lanzar la app. |
| **Conflicto en Git (Push Rejected)** | GitHub creó archivos (README/LICENSE) en la web que no existían localmente. | Se utilizó `git pull --allow-unrelated-histories` (o `push --force`) para sincronizar ambos repositorios. |
| **Errores de lectura en PDFs específicos** | Fragmentos demasiado grandes que confundían al modelo. | Se ajustó el `CHUNK_SIZE` y `CHUNK_OVERLAP` en la configuración para mejorar la precisión. |
| **Lentitud en la respuesta** | El modelo LLM requería muchos recursos de CPU/GPU. | Se optimizó el flujo de trabajo cargando los embeddings solo cuando es necesario. |

---

## 4. Conclusión
El proyecto cumple satisfactoriamente con los requisitos: es funcional, estéticamente profesional y mantiene un enfoque estricto en la seguridad de los datos al no depender de APIs externas. El sistema está listo para ser utilizado en entornos industriales o técnicos donde la confidencialidad es crítica.
