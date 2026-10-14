from fastapi import HTTPException

items_db = {
    'Soumya': {'name': 'Book', 'price': 29.99},
    'Ankita': {'name': 'Laptop', 'price': 1999.99},
    'Souvik': {'name': 'Keyboard', 'price': 49.99}
}

def read(name):
    if name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return items_db[name]