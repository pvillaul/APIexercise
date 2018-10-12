# Authors: Meyer Montagner, Pablo Villalba
# Programa que inicia un servidor usado como práctica del concepto de API.

from typing import Dict
from flask import Flask, jsonify, request

app = Flask(__name__)                           # type: Flask

userIdDictionary = {'1': 'Paco', '2': 'Pepe'}   # type: Dict[str, str]


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """Recibe desde la ruta el id de un usuario.
    Retorna un JSON con el usuario registrado con el id recibido."""
    user = userIdDictionary[user_id]  # type: str
    return jsonify(user)


@app.route('/concatenate/', methods=['GET'])
def concatenate():
    """Recibe por parámetros dos cadenas de caracteres.
    Retorna un JSON con las dos cadenas concatenadas."""
    string1 = request.args.get('string1')   # type: str
    string2 = request.args.get('string2')   # type: str
    result = string1 + string2              # type: str
    return jsonify(result)


@app.route('/calculate/<num>', methods=['GET'])
def calculate_square(num):
    """Recibe desde la ruta un número.
    Retorna un JSON con el cuadrado del número recibido."""
    num = float(num)          # type: float
    result = num * num        # type: float
    return jsonify(result)


@app.route('/calculate/', methods=['GET'])
def calculate_square_with_param():
    """Recibe como parámetro un número.
    Retorna un JSON con el cuadrado del número recibido."""
    num = request.args.get('num')   # type: str
    num = float(num)                # type: float
    result = num * num              # type: float
    return jsonify(result)


@app.route('/sayhello', methods=['GET'])
def say_hello():
    """Retorna un JSON con un string de saludo.
    No recibe parámetros."""
    var = 'hola'                    # type: str
    return jsonify(var)


if __name__ == "__main__":
    """Inicia la ejecución del servidor."""
    app.run(host='127.0.0.1', port=5000, debug=True)