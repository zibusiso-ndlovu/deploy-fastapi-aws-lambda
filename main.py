from fastapi import FastAPI, Path, Query
from mangum import Mangum
from typing import Optional, List

app = FastAPI()
handler = Mangum(app)

# Sample data
items = [
    {"id": 1, "name": "Item 1", "price": 10.99},
    {"id": 2, "name": "Item 2", "price": 20.49},
    {"id": 3, "name": "Item 3", "price": 15.99},
]

reviews = {
    1: ["Great item!", "Highly recommended"],
    2: ["Nice product", "Good value for money"],
    3: ["Not satisfied", "Needs improvement"]
}

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
]

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the FastAPI - AWS Lambda demo!"}

@app.get("/items/", tags=["Items"])
def get_items():
    return {"items": items}

@app.get("/items/{item_id}", tags=["Items"])
def get_item(item_id: int = Path(..., description="ID of the item to retrieve")):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return {"message": "Item not found"}
    return {"item": item}

@app.get("/items/{item_id}/reviews/", tags=["Items"])
def get_item_reviews(item_id: int = Path(..., description="ID of the item to retrieve")):
    if item_id not in reviews:
        return {"message": "No reviews found for this item"}
    return {"reviews": reviews[item_id]}

@app.get("/users/", tags=["Users"])
def get_users():
    return {"users": users}

@app.get("/users/by_name/", tags=["Users"])
def get_user_by_name(name: str = Query(..., description="Name of the user to retrieve")):
    filtered_users = [user for user in users if user["name"] == name]
    if not filtered_users:
        return {"message": "No user found with this name"}
    return {"users": filtered_users}

@app.get("/users/{user_id}", tags=["Users"])
def get_user(user_id: int = Path(..., description="ID of the user to retrieve")):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        return {"message": "User not found"}
    return {"user": user}