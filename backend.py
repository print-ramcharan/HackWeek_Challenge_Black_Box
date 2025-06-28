from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import base64
import random
import string

app = FastAPI()

# Shared countdown state
countdown_value = 8160000

class DataModel(BaseModel):
    data: Optional[str] = ""

# Countdown task
@app.on_event("startup")
async def start_countdown():
    from asyncio import create_task, sleep
    async def decrement():
        global countdown_value
        while countdown_value > 0:
            countdown_value -= 3
            await sleep(1)
    create_task(decrement())

# /data
@app.post("/data")
async def data_endpoint(item: DataModel):
    encoded = base64.b64encode(item.data.encode()).decode()
    return {"result": encoded}

# /zap
@app.post("/zap")
async def zap_endpoint(item: DataModel):
    no_digits = "".join([c for c in item.data if not c.isdigit()])
    return {"result": no_digits}

# /alpha
@app.post("/alpha")
async def alpha_endpoint(item: DataModel):
    if not item.data or len(item.data) == 0:
        return {"result": False}
    if item.data[0].isalpha():
        return {"result": True}
    return {"result": False}

# /glitch
@app.post("/glitch")
async def glitch_endpoint(item: DataModel):
    if len(item.data) % 2 == 0:
        # random permutation
        chars = list(item.data)
        random.shuffle(chars)
        return {"result": "".join(chars)}
    else:
        return {"result": item.data[::-1]}

# /fizzbuzz
@app.post("/fizzbuzz")
async def fizzbuzz_endpoint():
    return {"result": False}

# /time
@app.get("/time")
async def time_endpoint():
    return {"result": countdown_value}
