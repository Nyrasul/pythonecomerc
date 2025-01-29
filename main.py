from fastapi import FastAPI, HTTPException, Depends
from models import Product, User, Order
from crud import create_product, get_product, update_product, delete_product, create_user, get_user, create_order, get_orders_by_user
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId

app = FastAPI()

# Products
@app.post("/products/", response_model=Product)
async def add_product(product: Product):
    return await create_product(product)

@app.get("/products/{product_id}", response_model=Product)
async def read_product(product_id: str):
    product = await get_product(product_id)
    if product:
        return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.put("/products/{product_id}", response_model=Product)
async def modify_product(product_id: str, product: Product):
    return await update_product(product_id, product)

@app.delete("/products/{product_id}")
async def remove_product(product_id: str):
    return await delete_product(product_id)

# Users
@app.post("/users/", response_model=User)
async def register_user(user: User):
    return await create_user(user)

@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await get_user(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Orders
@app.post("/orders/", response_model=Order)
async def place_order(order: Order):
    return await create_order(order)

@app.get("/orders/{user_id}", response_model=list[Order])
async def read_orders(user_id: str):
    return await get_orders_by_user(user_id)
