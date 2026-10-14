from fastapi import FastAPI, HTTPException, Path, Query
from helper import read
app = FastAPI()


@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/{name}')
def read_name(name:str = Path(..., description="The name to be greeted")):
    return read(name)

@app.get("/items/{name}")
def read_item(name: str = Path(..., description="The name to be greeted"),price: float = Query(..., description="The price of the item"), author: str = Query(..., description="The author of the item")):
    # if name not in items_db:
    #     raise HTTPException(status_code=404, detail="Item not found")
    # else:
    return {"price":price, 'name':name, 'author':author}

