# ServidorPOOPython
Servidor en Python que responde a varios tipos de peticiones

## Arranque 
En el directorio del proyecto ejecutar las siguiente instrucción:

1. Activar el entorno virtual
   - Ir a la carpeta /venv/Scripts/
   - Ejecutar activate
   
2. Desde la carpeta principal
  - Ejecutar ``` set FLASK_APP=__init__.py ```
  - Ejecutar ``` set FLASK_ENV=development ```
  
3.Desde la carpeta principal ejecutar
 ``` flask run --host=0.0.0.0 --port=3002 ```

## Tipos de entidades
Hay dos tipos de entidades:
- LocalBusiness
- FoodEstablishment

## Estructura de LocalBusiness

| Atributos | Descripción | Tipo |
| ---- | ---- | ---- |
| name | Nombre del local  | Texto |
| address | Dirección del local | Texto |
| description | Descripción del local | Texto |
| telephone | Telefono del local | Texto |
| url | Url de la web del local | Texto |
| openingHours | Horas a las que esta abierto el local | Array de Textos |

## Estructura de FoodEstablishment

| Atributos | Descripción | Tipo |
| ---- | ---- | ---- |
| name | Nombre del local  | Texto |
| address | Dirección del local | Texto |
| description | Descripción del local | Texto |
| telephone | Telefono del local | Texto |
| url | Url de la web del local | Texto |
| openingHours | Horas a las que esta abierto el local | Array de Textos |
| acceptsReservations | Si acepta reservas | Booleano |
| servesCuisine | Tipos de cocina que sirve | Array de Textos |

## Estructura de las peticiones al servidor

| Estructura petición | Descripción |
| ---- | ---- |
| GET <url> | Devolverá información sobre los tipos de entidad disponibles |
| GET <url>/{entidad} | Mostrará la lista de todas las entidades de ese tipo. |
| POST <url>/{entidad} | Añadir una entidad pasándole los campos en el cuerpo codificados en JSON |
| PUT <url>/{entidad}/{id} | Actualizar la entidad con identificador {id}.En el cuerpo se incluirán los nuevos datos actualizados de esa entidad |
| GET <url>/{entidad}/{id} | Devuelve información de una entidad concreta |
| DELETE <url>/{entidad}/{id} | Borrar datos de una entidad concreta |

