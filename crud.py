from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from models import Product, User, Order
from connect import get_db
import bcrypt

# MongoDB connection
client = AsyncIOMotorClient("mongodb+srv://nurasyl0704:egdWWHkvBzucpOvf@cluster0.ibrcj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.ecommerce_db

# Products
async def create_product(product: Product):
    product_dict = product.dict()
    await db.products.insert_one(product_dict)
    return product_dict

async def get_product(product_id: str):
    product = await db.products.find_one({"_id": ObjectId(product_id)})
    return product

async def update_product(product_id: str, product: Product):
    await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict()})
    return await get_product(product_id)

async def delete_product(product_id: str):
    await db.products.delete_one({"_id": ObjectId(product_id)})
    return {"message": "Product deleted"}

# Users
async def create_user(user: User):
    user_dict = user.dict()
    user_dict["password"] = bcrypt.hashpw(user_dict["password"].encode("utf-8"), bcrypt.gensalt())
    await db.users.insert_one(user_dict)
    return user_dict

async def get_user(user_id: str):
    user = await db.users.find_one({"_id": ObjectId(user_id)})
    return user

# Orders
async def create_order(order: Order):
    order_dict = order.dict()
    await db.orders.insert_one(order_dict)
    return order_dict

async def get_orders_by_user(user_id: str):
    orders = await db.orders.find({"user_id": user_id}).to_list(100)
    return orders
