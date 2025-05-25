from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def index():
    return "Hola, esta API está desplegada en la nube 🚀"

@app.route('/sumar')
def sumar():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        return jsonify({"resultado": a + b})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/productos')
def productos():
    lista_productos = [
        {"id": 1, "nombre": "Laptop", "precio": 13500, "descripcion": "Laptop Lenovo 15”"},
        {"id": 2, "nombre": "Mouse", "precio": 350, "descripcion": "Mouse inalámbrico Logitech"},
        {"id": 3, "nombre": "Monitor", "precio": 3200, "descripcion": "Monitor Samsung 24 pulgadas"},
        {"id": 4, "nombre": "Teclado", "precio": 650, "descripcion": "Teclado mecánico RGB"},
    ]
    return jsonify(lista_productos)

# Esto es necesario para que Vercel reconozca la app
def handler(request, *args, **kwargs):
    from flask import Request
    return app(request.environ, start_response=kwargs.get('start_response'))

if __name__ == "__main__":
    app.run()
