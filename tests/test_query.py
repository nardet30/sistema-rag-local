import requests

def test_query():
    url = "http://localhost:8000/ask"
    data = {"question": "¿Qué es un sensor inductivo?"}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("Respuesta recibida:")
            print(response.json())
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error al conectar con la API: {e}")

if __name__ == "__main__":
    test_query()
