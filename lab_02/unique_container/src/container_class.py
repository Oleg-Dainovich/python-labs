import re
import pickle
import os

class UniqueContainer:
    _username: str
    _container: set[str] = set()
    _filename: str

    def __init__(self, username: str):
        self._username = username
        self._filename = f"{username}.dmp"

    def add(self, key: str):                            # user need to be able to input several keys 
        self._container.add(key)

    def remove(self, key: str):
        self._container.remove(key)

    def find(self, key:str):                            # user need to be able to input several keys
        return key in self._container

    def list(self):
        return list(self._container)

    def grep(self, regex):
        return list(filter(lambda key: re.match(regex, key), self._container))

    def save(self):
        with open(self._filename, "wb") as file:
            pickle.dump(self._container, file)

    def load(self):
        with open(self._filename, "rb") as file:
            loaded_set = pickle.load(file)
            self._container = self._container | loaded_set

    def is_exist(self):
        return os.path.exists(self._filename)
