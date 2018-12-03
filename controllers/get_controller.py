from flask import json, Blueprint, request
from flask_cors import cross_origin

from ..model import datos

__author__ = 'Ramon Sobrino'

routes = Blueprint( 'get', __name__ )

@routes.route( '/',methods=['GET'] )
@cross_origin()
def get_todos_info():
    string = '<section> <h3> Info de entidades </h3>'
    string += '<p>Hay dos tipos de entidades: </p>'
    string += '<ul><li>LocalBusiness</li><li>FoodEstablishment</li></ul>'
    string += '<h3> Entidad LocalBusiness </h3>'
    string += '<table><thead><tr><th>Atributos</th><th>Descripcion</th><th>Tipo</th></tr></thead><tbody><tr><td>name</td>'
    string += '<td>Nombre del local</td><td>Texto</td></tr><tr><td>address</td><td>Direccion del local</td><td>Texto</td>'
    string += '</tr><tr><td>description</td><td>Descripcion del local</td><td>Texto</td></tr><tr><td>telephone</td><td>Telefono del local</td>'
    string += '<td>Texto</td></tr><tr><td>url</td><td>Url de la web del local</td><td>Texto</td></tr><tr><td>openingHours</td><td>Horas a las que esta abierto el local</td>'
    string += '<td>Array de Textos</td></tr></tbody></table>'
    string += '<h3> Entidad FoodEstablishment </h3>'
    string += '<table><thead><tr><th>Atributos</th><th>Descripcion</th><th>Tipo</th></tr></thead><tbody><tr><td>name</td><td>Nombre del local</td>'
    string += '<td>Texto</td></tr><tr><td>address</td><td>Direccion del local</td><td>Texto</td></tr><tr><td>description</td><td>Descripcion del local</td>'
    string += '<td>Texto</td></tr><tr><td>telephone</td><td>Telefono del local</td><td>Texto</td></tr><tr><td>url</td><td>Url de la web del local</td>'
    string += '<td>Texto</td></tr><tr><td>openingHours</td><td>Horas a las que esta abierto el local</td><td>Array de Textos</td></tr><tr>'
    string += '<td>acceptsReservations</td><td>Si acepta reservas</td><td>Booleano</td></tr><tr><td>servesCuisine</td><td>Tipos de cocina que sirve</td>'
    string += '<td>Array de Textos</td></tr></tbody></table>'
    string += '</section>'
    return string


@routes.route( '/LocalBusiness', methods=['GET'] )
@cross_origin()
def get_todos_local():
    respuesta = ''
    for dato in datos:
        if dato.type == 'LocalBusiness':
            respuesta += accept(dato)
    return respuesta


@routes.route( '/FoodEstablishment', methods=['GET'] )
@cross_origin()
def get_todos_food():
    respuesta = ''
    for dato in datos:
        if dato.type == 'FoodEstablishment':
            respuesta += accept(dato)
    return respuesta


@routes.route( '/LocalBusiness/<int:number>', methods=['GET'] )
@cross_origin()
def get_local_id(number):
    respuesta = ''
    for dato in datos:
        if dato.type == 'LocalBusiness' and dato.id == number :
            respuesta += accept(dato)
    return respuesta


@routes.route( '/FoodEstablishment/<int:number>', methods=['GET'] )
@cross_origin()
def get_food_id(number):
    respuesta = ''
    for dato in datos:
        if dato.type == 'FoodEstablishment' and dato.id == number:
            respuesta += accept(dato)
    return respuesta



def accept(dato):
    if request.headers['Accept'] == 'application/xml':
        return dato.to_xml()
    elif request.headers['Accept'] == 'application/json':
        return dato.to_json()
    else:
        return dato.to_html()
