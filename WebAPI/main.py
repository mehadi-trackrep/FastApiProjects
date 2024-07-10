import json
import requests
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    currency: str
    tax: Optional[float] = None

async def fetch_coin_desc():
    return requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").text

app = FastAPI()

@app.get("/") # route. This is a decorator related to a `path operation`, or a `path operation decorator`.
async def root(): # path operation function
    return {"message": "Hello World"}

@app.post("/items/")
async def create_item(item: Item):
    item_dict = dict(item)
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    coin_desc = await fetch_coin_desc()
    item_dict = dict(item)
    item_dict.update({"coin_desc": json.loads(coin_desc)})
    return {"item_id": item_id, **item_dict}

