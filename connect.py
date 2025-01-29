from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = "mongodb+srv://nurasyl0704:egdWWHkvBzucpOvf@cluster0.ibrcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Replace with your actual URI

client = AsyncIOMotorClient(MONGODB_URI)
db = client.ecommerce_db

async def get_db():
    return db
