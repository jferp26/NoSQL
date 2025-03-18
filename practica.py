import pymongo

cliente=pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

db = cliente ["practica_7"]
productos= db ["productos"]
"""
numero_productos=input ("Introduzca el numero de productos a meter: ")
numero_productos_metidos=0
producto1 = {"nombre" : "laptop", "precio": 1000,"stock":5}

productos.insert_one(producto1)

productos.update_one({"nombre":"laptop"}, {"$set":{"precio":1300}})

laptop = productos.find_one({"nombre":"laptop"})
print (laptop)

"""

productos.delete_one({"nombre":"Tablet"})

tablet = productos.find_one({"nombre":"Tablet"})
print (tablet)