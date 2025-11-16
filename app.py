# app.py
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello, World!")


@app.route('/echo', methods=['POST'])
def echo():
    data = request.get_json(force=True)
    return jsonify(data), 201


@app.route('/reverse', methods=['POST'])
def reverse():
    data = request.get_json(force=True)
    text = data.get('text', '')
    return jsonify(reversed_text=text[::-1]), 201


@app.route('/square/<int:number>', methods=['GET'])
def square(number):
    return jsonify(square=number ** 2)


if __name__ == '__main__':
    app.run(debug=True)
