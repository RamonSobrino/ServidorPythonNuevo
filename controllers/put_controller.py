from flask import json, Blueprint,request
from flask_cors import cross_origin

from ..model import datos

__author__ = 'Dani Meana'

routes = Blueprint( 'put', __name__ )


@routes.route( '/LocalBusiness/<int:number>', methods=['PUT'] )
@cross_origin()
def delete_local_id(number):
    nuevo_objeto = json.loads( request.data )
    for dato in datos:
        if dato.type == 'LocalBusiness' and dato.id == number :
            dato.actualizar(nuevo_objeto)
            return 'PUT: LocalBusiness'
    return 'Objeto no encontrado', 400


@routes.route( '/FoodEstablishment/<int:number>', methods=['PUT'] )
@cross_origin()
def delete_food_id(number):
    nuevo_objeto = json.loads( request.data )
    for dato in datos:
        if dato.type == 'FoodEstablishment' and dato.id == number:
            dato.actualizar(nuevo_objeto)
            return 'PUT: FoodEstablishment'
    return 'Objeto no encontrado', 400


