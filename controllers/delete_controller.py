from flask import json, Blueprint, request
from flask_cors import cross_origin

from ..model import datos

routes = Blueprint( 'delete', __name__ )


@routes.route( '/LocalBusiness/<int:number>', methods=['DELETE'] )
@cross_origin()
def delete_local_id(number):
    for dato in datos:
        if dato.type == 'LocalBusiness' and dato.id == number :
            datos.remove(dato)
            return 'LocalBusiness borrado'
    return 'Objeto no encontrado', 400


@routes.route( '/FoodEstablishment/<int:number>', methods=['DELETE'] )
@cross_origin()
def delete_food_id(number):
    for dato in datos:
        if dato.type == 'FoodEstablishment' and dato.id == number:
            datos.remove(dato)
            return 'FoodEstablishment borrado'
    return 'Objeto no encontrado', 400


