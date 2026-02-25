import requests
import json

def check_ollama():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        if response.status_code == 200:
            models = [m['name'] for m in response.json().get('models', [])]
            print(f"Ollama está activo. Modelos disponibles: {models}")
            return True
        else:
            print("Ollama no parece estar respondiendo correctamente.")
            return False
    except Exception as e:
        print(f"Error al conectar con Ollama: {e}")
        return False

if __name__ == "__main__":
    check_ollama()
