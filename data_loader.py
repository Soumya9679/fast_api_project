import json

students = []

def load_data():
    with open("data/data.json", "r") as f:
        data = json.load(f)
        for i in data['students']:
            students.append(i)
        return students

def save_data(students):
    with open("data/data.json", "w") as f:
        json.dump(students, f, indent=4)
