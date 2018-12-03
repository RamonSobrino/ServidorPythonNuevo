from flask import json, Blueprint,request
from flask_cors import cross_origin

from ..model import FoodEstablishment, LocalBusiness
from ..model import datos

__author__ = 'Dani Meana'

routes = Blueprint( 'post', __name__ )


@routes.route( '/LocalBusiness', methods=['POST'] )
@cross_origin()
def post_local():
    respuesta = ''

    nuevo_objeto = json.loads( request.data )
    nuevo_id = 0
    for dato in datos:
        if dato.id > nuevo_id:
            nuevo_id = dato.id
    nuevo_id = nuevo_id+1
    if nuevo_objeto['@type'] == 'LocalBusiness':
        objeto = LocalBusiness(nuevo_objeto)
        objeto.id = nuevo_id
        datos.append(objeto)
        return 'LocalBusiness bien agregado'
    else:
        return 'LocalBusiness Mal agregado', 400


@routes.route( '/FoodEstablishment', methods=['POST'] )
@cross_origin()
def post_food():
    nuevo_objeto = json.loads( request.data )
    nuevo_id = 0
    for dato in datos:
        if dato.id > nuevo_id:
            nuevo_id = dato.id
    nuevo_id = nuevo_id + 1
    if nuevo_objeto['@type'] == 'FoodEstablishment':
        objeto = FoodEstablishment( nuevo_objeto )
        objeto.id = nuevo_id
        datos.append( objeto )
        return 'FoodEstablishment bien agregado'
    else:
        return 'FoodEstablishment Mal agregado', 400

