import json

students = []

def load_data():
    with open("data/data.json", "r") as f:
        data = json.load(f)
        for i in data['students']:
            students.append(i)
        return students

def save_data(students):
    student_data = {
        "students": students
    }
    with open("data/data.json", "w") as f:
        json.dump(student_data, f, indent=4)
