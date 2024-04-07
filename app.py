from flask import Flask
from flask_mongoengine import MongoEngine
    

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/imagenes'
app.secret_key = "123456789"
miConexion = pymongo.MongoClient('mongodb://localhost:27017/')
app.config['MONGODB_SETTINGS'] = [{
    "baseDatos": "GESTIONPRODUCTOS",
    "host": "localhost",
    "port": 27017
}]
baseDatos = MongoEngine(app)

'''
baseDatos = miConexion['GESTIONPRODUCTOS']
productos = baseDatos['PRODUCTOS']
categorias = baseDatos['CATEGORIAS']
usuarios = baseDatos['USUARIOS']
'''

from controlador.productoController import *
from controlador.categoriaController import *
from controlador.usuarioController import *


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
