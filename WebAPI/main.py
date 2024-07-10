from fastapi import FastAPI

app = FastAPI()

@app.get("/") # route. This is a decorator related to a `path operation`, or a `path operation decorator`.
async def root(): # path operation function
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}