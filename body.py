# Task 1
# Create a Pydantic model called User with:
# - username: str (required)
# - email: str (required)
# - age: int (required)
# - bio: str | None = None (optional)
# - is_active: bool = True (optional, defaults True)
#
# Create POST /users that accepts this model and returns it back
# Test in /docs with:
#   a) All fields provided
#   b) Only required fields
#   c) Missing a required field — observe the validation error

# Task 2
# Create a Pydantic model called Product with:
# - name: str (required)
# - price: float (required)
# - category: str (required)
# - discount: float = 0.0 (optional)
#
# Create POST /products that:
# - Accepts the Product model
# - Computes final_price = price - (price * discount / 100)
# - Returns the product dict PLUS the computed final_price
# Use model_dump() to build the response
# Test with discount=20 and without discount

# Task 3
# Create PUT /products/{product_id} that combines:
# - product_id: int (path)
# - A Product model from Task 2 (body)
# Return {"product_id": product_id, **product.model_dump()}
# Test in /docs — notice it shows both the path param AND body fields

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
#
# Inside the function:
# - Compute total = quantity * price
# - Return all path params, all body fields, notify, and total
# Test with and without the notify query parameter