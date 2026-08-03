import json

FILE_PATH = "data.json"

def read_data():
    with open(FILE_PATH, "r") as file:
        return json.load(file)

def write_data(data):
    with open(FILE_PATH, "w") as file:
        return json.dump(data, file, indent=4)