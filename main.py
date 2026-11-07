from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"helo": "world"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/sum")
def add(num1: float, num2: float):
    return {"sum": num1 + num2}