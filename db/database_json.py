import json
from typing import Any
from datetime import date
import os

class DatabaseJSON():       
    path: str = None
    data: Any = None
    def __init__(self, path: str = None) -> None:
        if path == None: # Create a new file. if it does not exist
            self.path = "db/data/JournalEntry.json"
            if os.path.isfile(self.path):
                self.data = self.load_json_file(self.path)
            else:
                self.create_json_file(self.path, {
                "app" : "Journal Entry",
                "date": f"{date.today()}"
            })
        else:
            self.path = path
            self.data = self.load_json_file(path)


    def create_json_file(self, path, data):
        self.path = path
        with open(f"{path}", 'w') as file:
            json.dump(data, file, indent=4)
        
        self.data = self.load_json_file(path)



    def load_json_file(self, path) -> Any:
        with open(f'{path}', 'r') as file:
            return json.load(file)
        


    def edit_json_file(self, key, value):
        data = self.getData()
        data[key] = value
        self.create_json_file(self.path, data)



    # Save data into json file.
    def save_json_file(self):
        json.dump(self.data, self.path, indent=4)

    def add_element(self ,key, new_element):
        self.data = self.load_json_file(self.path)
        if key in self.data and isinstance(self.data[key], list):
            # Check existence of the new element
            for i in self.data[key]:
                if i == new_element:
                    print(f"{new_element} Element already exists.")
                    return
            self.data[key].append(new_element)
        else:
            self.data[key] = [new_element]

        self.create_json_file(self.path, self.data)
        print(f"Element '{new_element}' added to '{key}'.")

    def getData(self, key:str = None) -> Any:
        if self.data == None:
            raise ImportError("Couldn't load data.")
        try:
            if key != None:
                return self.data[key]
        except Exception as e:
            print(e)
        return self.data