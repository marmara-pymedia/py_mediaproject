import json
from entities.Type import Type

class TypeService:
    def __init__(self):
        pass

    def get_all(self)->list[Type]:
        with open("data/types.json","r") as file:
            types=json.load(file)
        return [Type(**type) for type in types]