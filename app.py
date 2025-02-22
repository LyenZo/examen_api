from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS
from flasgger import Swagger
import random

# Cargar variables de entorno
load_dotenv()

# Crear instancia de Flask
app = Flask(__name__)
CORS(app)

# Configuración de Swagger
app.config['SWAGGER'] = {
    'title': 'Mi API Flask',
    'uiversion': 3
}
swagger = Swagger(app)

# Datos ficticios simulando usuarios
users = [
    {"id": 1, "nombre": "Alice", "edad": 25},
    {"id": 2, "nombre": "Bob", "edad": 30},
    {"id": 3, "nombre": "Charlie", "edad": 35},
    {"id": 4, "nombre": "David", "edad": 40},
    {"id": 5, "nombre": "Eva", "edad": 45},
    {"id": 6, "nombre": "Frank", "edad": 50},
    {"id": 7, "nombre": "Grace", "edad": 55},
    {"id": 8, "nombre": "Hank", "edad": 60},
    {"id": 9, "nombre": "Ivy", "edad": 65},
    {"id": 10, "nombre": "Jack", "edad": 70},
]

# Ruta para obtener 5 registros aleatorios
@app.route('/users', methods=['GET'])
def get_random_users():
    sample_users = random.sample(users, 5)  # Selecciona 5 registros aleatorios
    return jsonify(sample_users)

if __name__ == '__main__':
    app.run(debug=True)
