from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "API Flask funcionando en Vercel 🚀"

@app.route('/sumar')
def sumar():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return jsonify({"resultado": a + b})

@app.route('/productos')
def productos():
    return jsonify([
        {"id": 1, "nombre": "Laptop", "precio": 13500},
        {"id": 2, "nombre": "Mouse", "precio": 350}
    ])
