#importaciones de Flask
from types import MethodType
from flask import Flask, request, jsonify
from flask_cors import CORS
from Gestor import Gestor
#importaciones aparte
from Publicaciones import Publicacion
from Usuarios import Usuario
import json
import re

#crear la app
app= Flask(__name__)
app.config["DEBUG"]=True
CORS(app)
gestor=Gestor()

# EndPoints
@app.route('/',methods=['GET'])
def home():
    return 'SERVER IS WORKING !!!'

@app.route('/obtenerusuarios')
def obtenerusuarios():
    return gestor.obtener_usuarios()

@app.route('/obtenerusuario/<string:emailx>',methods=['GET']) #para encontrar solo un usuario
def obtenerusuariox(emailx):
    return gestor.obtenerusuario(emailx)    

@app.route('/obtenerpublicaciones')
def obtenerpublicaciones():
    return gestor.obtener_publicacion()

@app.route('/crearusuario', methods=['POST'])
def crearusuario():
    dato=request.json
    gestor.crearUsuario(dato['name'],dato['gender'],dato['username'],dato['email'],dato['password'])
    return '{"Estado":"Usuario Creado"}'

@app.route('/crearpublicacion', methods=['POST'])
def crearpublicacion():
    dato = request.json
    gestor.crearPublicacion(dato['type'],dato['url'],dato['date'],dato['category'])
    return '{"Estado":"Publicacion realizada"}'

@app.route('/eliminarpublicacion/<url>',methods=['DELETE'])
def eliminarpublicacion(url):
    if(gestor.eliminar_publicacion(url)):
         return '{"data":"Publicacion eliminada"}'
    return '{"data":"Error"}'

@app.route('/eliminarusuario/<username>/<mail>',methods=['DELETE'])
def eliminarusuario(username,mail):
    if(gestor.eliminar_usuario(username,mail)):
         return '{"data":"Usuario eliminado"}'
    return '{"data":"Error"}'

@app.route('/actualizarusuario/<string:email>',methods=['PUT'])
def actualizarusuario(email):
    dato = request.json
    if gestor.actualizar_usuarios(dato['name'],dato['gender'],dato['username'],dato['email'],dato['password']):
        return '{"data":"Actualizado"}'
    return '{"data":"Error"}'


@app.route('/actualizarpublicacion/<url>',methods=['PUT'])
def actualizarpublicacion(url):
    dato = request.json
    if gestor.actualizar_publicaciones(dato['type'],dato['url'],dato['date'],dato['category']):
        return jsonify({"data":"Actualizado"})
    return jsonify({"data":"Error"})


@app.route('/login/<string:user>/<string:password>')
def login(user,password):
    return gestor.iniciar_sesion(user,password)
        

@app.route('/registro',methods=['POST'])
def registrar():
    dato = request.json
    gestor.registrar_usuario(dato['name'],dato['gender'],dato['username'],dato['email'],dato['password'])    
    return '{"data":"Creado"}'

@app.route('/carga',methods=['POST'])
def carga():
    dato = request.json
    gestor.cargamasiva(dato['data'])
    return '{"data":"Cargados"}'

#INICIAR EL SERVIDOR 

if __name__== "__main__":
    app.run(host="0.0.0.0", debug=True)

