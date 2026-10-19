import json
import os

resources = [
  {"id": "R001", "name": "Laptop", "category": "Electronics", "total": 10, "available": 10},
  {"id": "R002", "name": "Keyboard", "category": "Accessories", "total": 5, "available": 5},
  {"id": "R003", "name": "Headset", "category": "Accessories", "total": 3, "available": 3}
]
fellows = {"F001": "Ada", "F002": "John", "F003": "Grace"}
borrow_records = []

Data_File = "campus_resoures.json"

def Save_data():
    data = {
        "resoures": resources,
        "borrow_resources": borrow_resources
    }
    try:
        with open(Data_File, "w") as f:
            json = dump