from flask import Flask, jsonify
from dotenv import dotenv_values

config= dotenv_values('.env')


app = Flask(__name__)

@app.route('/')

def hello_world():
    return "Hola Mundo"

if __name__ == '__main__': app.run(host='localhost', port=config["PORT"], debug=True)
