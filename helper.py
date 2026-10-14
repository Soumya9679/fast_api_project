from fastapi import HTTPException
from data_loader import load_data, save_data

def read(name):
    students = load_data()
    for student in students:
        if student['name'] == name:
            return student
    raise HTTPException(status_code=404, detail="Item not found")

def add(student):
    students = load_data()
    student['id'] = len(students) + 1
    for i in students:
        if i['id'] == student['id']:
            raise HTTPException(status_code=400, detail="Student with this id already exists")
    students.append(student)
    save_data(students)
    return student

def delete(name):
    students = load_data()
    for student in students:
        if student['name'] == name:
            students.remove(student)
            save_data(students)
            return student
    raise HTTPException(status_code=404, detail="Item not found")


