

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

mongodb_uri = os.getenv('MONGODB_URI')
# Create a new client and connect to the server
client = MongoClient(mongodb_uri, server_api=ServerApi('1'))

db = client.Republica_Dominicana
collection = db.Provincias

# Consultar todas las provincias y mostrarlas en pantalla
Provincias = collection.find()


if mongodb_uri is None:
    print("La variable de entorno 'MONGODB_URI' no está definida.")

else:
    print("Listado de provincias dominicanas:")
    for provincia in Provincias:
        print(provincia["nombre"])

# Cerrar la conexión
client.close()

