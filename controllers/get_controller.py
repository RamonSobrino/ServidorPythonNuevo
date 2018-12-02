from flask import json, Blueprint, request
from flask_cors import cross_origin

from ..model import datos

__author__ = 'Ramon Sobrino'

routes = Blueprint( 'get', __name__ )


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
