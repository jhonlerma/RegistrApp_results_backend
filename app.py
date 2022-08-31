from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv, dotenv_values
from routes.candidate_routes import candidate_module
from routes.political_party_routes import political_party_module
from routes.result_routes import result_module
from routes.table_routes import table_module
# se cargan las configuraciones por defecto del archivo .env en la raiz del proyecto
# load_dotenv() 

# se puede personalizar la ruta y el archivo .env para cargarlo desde otra localizacion o archivo
config = dotenv_values(".env")
app = Flask(__name__)
cors = CORS(app)

# importar rutas de candidates
app.register_blueprint(candidate_module, url_prefix='/candidate')
app.register_blueprint(political_party_module, url_prefix="/political_party")
app.register_blueprint(result_module, url_prefix="/result")
app.register_blueprint(table_module, url_prefix="/table")


@app.route('/')
def hello_world():
    diccionario = {'mensaje':'Hola mundo!'}
    return jsonify(diccionario)

if __name__ == '__main__':
    app.run(host="localhost", port=config["PORT"], debug=True)
