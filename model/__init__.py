
import json

from .food_establishment import FoodEstablishment
from .local_business import LocalBusiness

archive = open('model/Objetos.json', 'r')
string = archive.read()
objects = json.loads(string)
id = 0
datos = []
for object in objects:
    if object['@type'] == 'FoodEstablishment':
        nuevo = FoodEstablishment(object)
        nuevo.id = id
        id =  id +1
        datos.append(nuevo)
    elif object['@type'] == 'LocalBusiness':
        nuevo = LocalBusiness(object)
        nuevo.id = id
        id =  id +1
        datos.append(nuevo)



