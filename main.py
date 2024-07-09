

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://holylady1304:Prueba0102@clusterhg.h4ladx5.mongodb.net/?retryWrites=true&w=majority&appName=ClusterHG"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.Republica_Dominicana
collection = db.Provincias

# Consultar todas las provincias y mostrarlas en pantalla
Provincias = collection.find()

print("Listado de provincias dominicanas:")
for provincia in Provincias:
    print(provincia["nombre"])

# Cerrar la conexión
client.close()

