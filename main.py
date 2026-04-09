from pymongo import MongoClient

uri = "mongodb+srv://sicexo1489_db_user:eKgZ23F0P2OrDGBl@distribuida.kvsrlty.mongodb.net/?appName=Distribuida"

client = MongoClient(uri)

# probar conexión
try:
    client.admin.command('ping')
    print("✅ Conectado a MongoDB Atlas")
except Exception as e:
    print("❌ Error:", e)