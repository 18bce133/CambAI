from fastapi import HTTPException, FastAPI
from huey import RedisHuey
from pydantic import BaseModel, ValidationError
import redis

app = FastAPI()
huey = RedisHuey('my-app',host='redis', port=6379)

try:
    r = redis.Redis(host='redis', port=6379)
except redis.ConnectionError:
    print("Could not connect to Redis server.")

class Item(BaseModel):
    item_value: str

@app.post("/items/{item_id}")
async def write_item(item_id: str, item: Item):
    try:
        item_data = item
    except ValidationError as e:
        raise HTTPException(422, detail=str(e))

    if item_data.item_value is None:
        raise HTTPException(422, detail="Item value is missing")
    elif item_data.item_value == "":
        raise HTTPException(400, detail="Item value is empty")
    else:
        try:
            write_key_value(item_id, item_data.item_value)
        except Exception as e:
            raise HTTPException(500, detail="An error occurred while writing to Redis.")
        return {"item_id": item_id, "item_value": item_data.item_value}

@huey.task()
def write_key_value(key: str, value: str):
    try:
        r.set(key, value)
    except redis.ConnectionError:
        print("Could not connect to Redis server.")

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    try:
        value = r.get(item_id)
    except redis.ConnectionError:
        raise HTTPException(500, detail="Could not connect to Redis server.")
    if value is None:
        raise HTTPException(404, detail="Item not found")
    return {"item_id": item_id, "item_value": value}
