from fastapi import FastAPI, HTTPException, Path, Query, Body
from helper import read, add
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

@app.post('/add')
def add_student(name:str = Body(..., description="The name of the student"), age:int = Body(..., description="The age of the student"), gender:str = Body(..., description="The gender of the student"), email:str = Body(..., description="The email of the student"), phone:str = Body(..., description="The phone number of the student"), course:str = Body(..., description="The course of the student"), semester:int = Body(..., description="The semester of the student"), cgpa:float = Body(..., description="The cgpa of the student"), city:str = Body(..., description="The city of the student")):
    student = {
        "name": name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "course": course,
        "semester": semester,
        "cgpa": cgpa,
        "city": city
    }
    add(student)