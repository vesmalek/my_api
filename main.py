from fastapi import FastAPI

app = FastAPI()

# Task 1
# Create GET /products with two optional query parameters:
# skip: int = 0 and limit: int = 5
# Use this hardcoded list as your data:
# products = ["shirt", "shoes", "hat", "belt", "socks", "watch", "bag", "jacket"]
# Return the sliced list based on skip and limit
# Test:
#   /products             → first 5 items
#   /products?skip=3      → items from index 3
#   /products?skip=2&limit=3  → 3 items starting from index 2


products = ["shirt", "shoes", "hat", "belt", "socks", "watch", "bag", "jacket"]

@app.get("/products")
async def get_products(skip: int = 0, limit: int = 5):
    return products[skip: skip + limit]




# Task 2
# Create GET /products/{product_id} with:
# - product_id as a path parameter (int)
# - search as an optional query parameter (str | None = None)
# - in_stock as a bool query parameter defaulting to True
# Return all three values in a dict
# Test:
#   /products/5                          → search is None, in_stock is True
#   /products/5?search=blue              → search has a value
#   /products/5?in_stock=false           → in_stock is False
#   /products/5?search=large&in_stock=1  → both set

@app.get("/products/{product_id}")
async def get_product(product_id: int, in_stock: bool = True ,search: str | None = None):
    return {
        "product_id": product_id,
        "in_stock": in_stock,
        "search": search
    }



# Task 3
# Create GET /orders with a REQUIRED query parameter called status: str
# No default value — it must be provided
# Return {"orders_with_status": status}
# Test:
#   /orders              → should return a validation error
#   /orders?status=paid  → should work

@app.get("/orders")
async def get_orders(status: str):
    return {"orders_with_status": status}

# Task 4 — Combine everything
# Create GET /users/{user_id}/products with:
# - user_id: int (path)
# - category: str (required query — no default)
# - skip: int = 0 (optional)
# - limit: int = 10 (optional)
# - active_only: bool = True (optional)
# Return all five values in a dict
# Test with at least 3 different URL combinations
# Open /docs and test from the interactive interface too