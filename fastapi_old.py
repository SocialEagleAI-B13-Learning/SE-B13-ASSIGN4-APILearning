import fastapi_old
from fastapi_old import fastapi_old
app = fastapi_old()

app.get("/")
def read_root():
    return{"helo":"world"}
app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return{"item_id":item_id,"q":q}