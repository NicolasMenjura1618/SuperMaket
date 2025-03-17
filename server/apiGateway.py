from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configuración de los microservicios
CHATBOT_SERVICE_URL = "http://localhost:5001"
PRODUCTS_SERVICE_URL = "http://localhost:5002"

@app.route("/chatbot", methods=["POST"])
def chatbot():
    """Redirige la consulta al chatbot service y maneja errores correctamente."""
    data = request.get_json()

    if not data or "pregunta" not in data or "product_id" not in data:
        return jsonify({"error": "Faltan parámetros en la solicitud."}), 400

    try:
        response = requests.post(f"{CHATBOT_SERVICE_URL}/chat", json=data)

        # Manejo de respuesta vacía o fallida
        if response.status_code != 200 or not response.text.strip():
            return jsonify({"error": "No se obtuvo respuesta válida del chatbot."}), 500
        
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al comunicarse con el chatbot: {e}")
        return jsonify({"error": "No se pudo conectar con el chatbot."}), 500

@app.route("/productos", methods=["GET", "POST"])
def productos():
    """Redirige la consulta al servicio de productos."""
    try:
        if request.method == "GET":
            response = requests.get(f"{PRODUCTS_SERVICE_URL}/productos")
        else:
            data = request.get_json()
            response = requests.post(f"{PRODUCTS_SERVICE_URL}/productos", json=data)
        
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        print(f"❌ Error al comunicarse con el servicio de productos: {e}")
        return jsonify({"error": "No se pudo conectar con el servicio de productos."}), 500

if __name__ == "__main__":
    print("🚀 API Gateway iniciado en http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
