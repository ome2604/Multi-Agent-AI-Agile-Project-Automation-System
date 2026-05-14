import json
from pathlib import Path


class LongTermMemory:

    def __init__(self):

        self.memory_file = Path("memory/project_memory.json")

        if not self.memory_file.exists():

            self.memory_file.write_text("{}")

    def save(self, key, value):

        data = self.load_all()

        data[key] = value

        with open(self.memory_file, "w") as file:

            json.dump(data, file, indent=4)

    def load(self, key):

        data = self.load_all()

        return data.get(key)

    def load_all(self):

        with open(self.memory_file, "r") as file:

            return json.load(file)