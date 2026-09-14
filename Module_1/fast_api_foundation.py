from fastapi import FastAPI
from fastapi import Request
import uvicorn 

app = FastAPI(
    title="Ayush Gupta Ka FastAPI",
    description="This is a FastAPI project created by Ayush Gupta",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

@app.get("/")
async def root():
    """Root endpoint that returns a welcome message and health status."""
    return {"message": "this is my first Backend Route OR end Point","status": "healthy"}

@app.get("/about")
async def about():
    """About endpoint that returns information about the application."""
    return { "server": "FastAPI", "version": "1.0.0", "author": "Ayush Gupta" }

@app.get("/orders")
async def get_orders():
    """Orders endpoint that returns a list of orders."""
    return {
        "orders": [
            {"id": "id 1", "item": "butter Chicken", "price": 200, "quantity": 1, "status": "delivered"},
            {"id": "id 2", "item": "Paneer Butter Masala", "price": 250, "quantity": 1, "status": "preparing"},
            {"id": "id 3", "item": "Dal Makhani", "price": 150, "quantity": 1, "status": "delivered"},
        ]
    }

@app.get("/orders/status1/{status}")
async def get_orders_by_status(status: str):
    """Orders endpoint that returns a list of orders filtered by status."""
    all_orders = [
        {"id": "id 1", "item": "butter Chicken", "price": 200, "quantity": 1, "status": "delivered"},
        {"id": "id 2", "item": "Paneer Butter Masala", "price": 250, "quantity": 1, "status": "preparing"},
        {"id": "id 3", "item": "Dal Makhani", "price": 150, "quantity": 1, "status": "delivered"},
    ]
    filtered_orders = [order for order in all_orders if order["status"] == status]
    return {"orders": filtered_orders}

@app.get("/orders/status")
async def order_status():
    """Get Order Status"""
    return {
        "total_today": 2_304_23,
        "top_city": "Delhi",
        "top_item": "Butter Chicken",
    }
@app.get("/debug/request-info")
async def request_info(request: Request):
    """Endpoint to return request information for debugging purposes."""
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host if request.client else None,
        "query_params": dict(request.query_params),
    } 

@app.get(
    "/orders/active",
    summary = "Get Active Orders",
    description = """Return all order that are currently being
    prepared"""
    "or are out for deleivery",
    
tags = ["Orders"],
response_description = "List of active orders",
deprecated = False
)

def get_active_orders():
    """Get Active Orders"""
    return {
        "active_orders": [
            {"id": "id 2", "item": "Paneer Butter Masala", "price": 250, "quantity": 1, "status": "preparing"},
            {"id": "id 4", "item": "Chicken Biryani", "price": 300, "quantity": 1, "status": "out for delivery"},
        ]
    }
@app.get("/resturants",tags=["Resturants"])
def list_restaurants():
    """List all restaurants"""
    return {
        "restaurants": [
            {"id": "id 1", "name": "Tasty Bites", "cuisine": "Indian", "rating": 4.5},
            {"id": "id 2", "name": "Burger Palace", "cuisine": "American", "rating": 4.2},
        ]
    }
@app.get("/resturants/MITS",tags=["Resturants"])
def list_restaurants_Mits():
    """List all restaurants"""
    return {
        "restaurants": [
            {"id": "id 1", "name": "Tasty Bites", "cuisine": "Indian", "rating": 4.5},
            {"id": "id 2", "name": "Burger Palace", "cuisine": "American", "rating": 4.2},
        ]
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fast_api_foundation:app", host="127.0.0.2", port=8000,reload=True)