import random
from pymongo import MongoClient
from datetime import datetime, timedelta

# Conectar a MongoDB (ajusta la URL si es necesario)
client = MongoClient("mongodb://admin:admin123@localhost:27017/")
db = client["practica_6"]

# 🔹 Colección de Clientes
clientes_nombres = ["Carlos", "Ana", "Luis", "Marta", "Pedro", "Lucía", "Javier", "Elena", "Manuel", "Sofía"]
ciudades = ["Madrid", "Barcelona", "Sevilla", "Valencia", "Bilbao", "Zaragoza", "Málaga", "Murcia", "Palma", "Valladolid"]

clientes = []
for i in range(20):  # 20 clientes únicos
    cliente = {
        "_id": i + 1,  # ID numérico para facilitar referencias
        "nombre": random.choice(clientes_nombres),
        "ciudad": random.choice(ciudades),
        "email": f"cliente{i+1}@example.com",
        "telefono": f"6{random.randint(10000000, 99999999)}"
    }
    clientes.append(cliente)

db.clientes.insert_many(clientes)

# 🔹 Colección de Ventas
productos = ["Laptop", "Móvil", "Tablet", "Monitor", "Teclado", "Ratón", "Impresora", "Auriculares", "Disco Duro", "Tarjeta Gráfica"]
categorias = ["Electrónica", "Accesorios", "Componentes", "Periféricos"]

ventas = []
for _ in range(50):  # 50 ventas
    venta = {
        "fecha": (datetime.now() - timedelta(days=random.randint(1, 365))).strftime("%Y-%m-%d"),
        "producto": random.choice(productos),
        "categoria": random.choice(categorias),
        "cliente_id": random.randint(1, 20),  # Relacionado con la colección de clientes
        "cantidad": random.randint(1, 10),
        "precio": round(random.uniform(50, 2000), 2)
    }
    ventas.append(venta)

db.ventas.insert_many(ventas)

# 🔹 Colección de Pedidos
pedidos = []
for i in range(30):  # 30 pedidos únicos
    pedido = {
        "_id": i + 1,  # ID numérico para facilitar referencias
        "cliente_id": random.randint(1, 20),  # Relacionado con la colección de clientes
        "fecha": (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d"),
        "productos": [
            {"nombre": random.choice(productos), "cantidad": random.randint(1, 5)},
            {"nombre": random.choice(productos), "cantidad": random.randint(1, 5)}
        ],
        "total": round(random.uniform(100, 5000), 2),
        "estado": random.choice(["Pendiente", "Enviado", "Entregado", "Cancelado"])
    }
    pedidos.append(pedido)

db.pedidos.insert_many(pedidos)

# Contar los documentos insertados
print(f"Se han insertado {db.clientes.count_documents({})} clientes en la colección 'clientes'.")
print(f"Se han insertado {db.ventas.count_documents({})} ventas en la colección 'ventas'.")
print(f"Se han insertado {db.pedidos.count_documents({})} pedidos en la colección 'pedidos'.")
