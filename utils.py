import json


def load_data(filename: str):
    with open(filename, "r") as file:
        output = json.load(file)
    return output