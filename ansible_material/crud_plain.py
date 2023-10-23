# Importing necessary modules
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.middleware.cors import CORSMiddleware
import uuid

# Instantiating FastAPI application
app = FastAPI()

# Adding CORS middleware to the application to handle Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Establishing connection to MongoDB on startup
@app.on_event("startup")
async def startup_event():
    """Initializes MongoDB client and database when the server starts."""
    app.state.mongodb = AsyncIOMotorClient('mongodb://localhost:27017')
    app.state.db = app.state.mongodb['my_database']

# Closing connection to MongoDB on shutdown
@app.on_event("shutdown")
async def shutdown_event():
    """Closes MongoDB client when the server shuts down."""
    app.state.mongodb.close()

# GET endpoint to fetch all items in the 'test_collection' collection
@app.get("/items/")
async def read_items():
    """Fetches all documents in the 'test_collection' collection."""
    items = []
    cursor = app.state.db['test_collection'].find()
    async for document in cursor:
        # Convert ObjectId to string
        document["_id"] = str(document["_id"])
        items.append(document)
    return items

# GET endpoint to fetch a specific item by its id
@app.get("/items/{item_id}")
async def read_item(item_id: str):
    """Fetches a single document in the 'test_collection' collection by its 'id'."""
    item = await app.state.db['test_collection'].find_one({"id": item_id})
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    # Convert ObjectId to string
    item["_id"] = str(item["_id"])
    return item

# POST endpoint to create a new item in the 'test_collection' collection
@app.post("/items/")
async def create_item(item: dict):
    """Creates a new document in the 'test_collection' collection."""
    # Add a unique id to the item
    item["id"] = str(uuid.uuid4())
    new_item = await app.state.db['test_collection'].insert_one(item)
    return {"item_id": str(new_item.inserted_id)}

# PUT endpoint to update an existing item by its id
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: dict):
    """Updates a specific document in the 'test_collection' collection by its 'id'."""
    item['id'] = item_id
    updated_item = await app.state.db['test_collection'].replace_one({"id": item_id}, item)
    if updated_item.matched_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}

# DELETE endpoint to delete an item by its id
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    """Deletes a specific document in the 'test_collection' collection by its 'id'."""
    deleted_item = await app.state.db['test_collection'].delete_one({"id": item_id})
    if deleted_item.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id}


