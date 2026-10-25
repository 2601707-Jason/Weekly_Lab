import os
import json
from inventory import Inventory

class File:
    def __init__(self, file):
        self.__file = file
    
    def exists(self) -> bool:
        return os.path.exists(self.__file)
    
    def load_inventory(self):
        with open(self.__file, mode="r", encoding="utf-8") as file:
            return json.load(file) 
    
    def save_inventory(self, inventory: Inventory):
        with open(self.__file, mode="w") as file:
            json.dump(inventory, file, indent=2)