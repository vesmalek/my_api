from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

# Task 1
# Create a Pydantic model called User with:
# - username: str (required)
# - email: str (required)
# - age: int (required)
# - bio: str | None = None (optional)
# - is_active: bool = True (optional, defaults True)

class User(BaseModel):
    username: str
    email: str
    age: int 
    bio: str | None = None
    is_active: bool = True

# Create POST /users that accepts this model and returns it back
# Test in /docs with:
#   a) All fields provided
#   b) Only required fields
#   c) Missing a required field — observe the validation error

@app.post("/users")
async def get_users(users: User):
    return users

# Task 2
# Create a Pydantic model called Product with:
# - name: str (required)
# - price: float (required)
# - category: str (required)
# - discount: float = 0.0 (optional)

class Product(BaseModel):
    name: str
    price: float
    category: str
    discount: float = 0.0

# Create POST /products that:
# - Accepts the Product model
# - Computes final_price = price - (price * discount / 100)
# - Returns the product dict PLUS the computed final_price
# Use model_dump() to build the response
# Test with discount=20 and without discount

@app.post("/products")
async def get_products(products: Product):
    final_price = products.price - (products.price * products.discount / 100)
    return {**products.model_dump(), "final_price": final_price,}

# Task 3
# Create PUT /products/{product_id} that combines:
# - product_id: int (path)
# - A Product model from Task 2 (body)
# Return {"product_id": product_id, **product.model_dump()}
# Test in /docs — notice it shows both the path param AND body fields

@app.put("/products/{product_id}")
async def get_product(product_id: int, products: Product):
    return {"product_id": product_id, **products.model_dump()}

# Task 4 — Combine all three
# Create PUT /users/{user_id}/orders/{order_id} with:
# - user_id: int (path)
# - order_id: int (path)
# - A Pydantic model called OrderUpdate:
#     product_name: str (required)
#     quantity: int (required)
#     price: float (required)
#     note: str | None = None
# - notify: bool = False (query parameter)

class OrderUpdate(BaseModel):
    product_name: str
    quantity: int
    price: float
    note: str | None = None

# Inside the function:
# - Compute total = quantity * price
# - Return all path params, all body fields, notify, and total
# Test with and without the notify query parameter

@app.put("/users/{user_id}/orders/{order_id}")
async def get_user_order(user_id: int, order_id: int, order: OrderUpdate, notify: bool = False):
    total = order.quantity * order.price
    return {
        "user_id": user_id,
        "order_id": order_id,
        **order.model_dump(),
        "notify": notify,
        "total": total
    }