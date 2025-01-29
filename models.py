from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    category: str
    stock: int

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: str = "user"

class Order(BaseModel):
    user_id: str
    product_ids: List[str]
    order_status: str = "pending"
    timestamp: datetime = datetime.utcnow()
