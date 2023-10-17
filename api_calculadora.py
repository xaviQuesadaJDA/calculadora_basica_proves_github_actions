#!/usr/bin/python3

"""
API-REST per servir la Calculadora basica
"""

__author__ = "Xavi"

from flask import Flask, jsonify
from calculadora import Calculadora


app = Flask(__name__)
calc = Calculadora()

@app.route("/")
def home():
    return "Benvingut a la calculadora"

@app.route("/suma/<p1>/<p2>")
def suma(p1, p2):
    return jsonify({"resultat": calc.suma(int(p1), int(p2))})

@app.route("/resta/<p1>/<p2>")
def resta(p1, p2):
    return jsonify({"resultat": calc.resta(int(p1), int(p2))})

@app.route("/multiplica/<p1>/<p2>")
def multiplica(p1, p2):
    return jsonify({"resultat": calc.multiplica(int(p1), int(p2))})

@app.route("/divideix/<p1>/<p2>")
def divisio(p1, p2):
    return jsonify({"resultat": calc.divisio(int(p1), int(p2))})
if __name__ == "__main__":
    app.run()
