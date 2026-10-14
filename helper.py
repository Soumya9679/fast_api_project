from fastapi import HTTPException
from data_loader import load_data
from data_loader import save_data

def read(name):
    students = load_data()
    for student in students:
        if student['name'] == name:
            return student
    raise HTTPException(status_code=404, detail="Item not found")

def add(student):
    students = load_data()
    students.append(student)
    save_data(students)
    return student

    