import re

from container_class import UniqueContainer

class ContainerController:
    _container_class: UniqueContainer = None

    def __init__(self):
        self.switch()

    @staticmethod
    def _split_and_apply(keys: str, function: callable):
        for key in keys.split():
            function(key)

    def add(self, args: str):
        if not args:
            print("No keys for add.")
            return
        
        self._split_and_apply(args, self._container_class.add)
        print("Keys added.")

    def _remove_key(self, key: str):
        if self._container_class.find(key):
            self._container_class.remove(key)
        else:
            print("Key doesnt exist.")

    def find(self, args: str):
        if not args:
            print("No keys for find.")

        self._split_and_apply(args, lambda key: print(f"Key {'' if self._container_class.find(key) else 'not '}exisits."))


    def remove(self, args: str):
        if not args:
            print("No keys for remove.")
            return
        
        self._split_and_apply(args, self._remove_key)

    def list(self, args):
        data = self._container_class.list()
        if not data:
            print("Empty.")
            return
        print(" ".join(data))

    def grep(self, args: str):
        if not args:
            print("No regex.")
            return
        
        try:
            regex = re.compile(args)
        except re.error:
            print("Incorrect regex.")
            return
        
        keys_found = self._container_class.grep(regex)

        if not keys_found:
            print("No such elements.")
            return
        
        print(" ".join(keys_found))

    def save(self, args):
        self._container_class.save()
        print('Saved successfully')

    def load(self, args):
        self._container_class.load()
        print('Loaded successfully')

    def exit(self, args):
        self._ask_for_save()
        exit(0)

    def _ask_for_save(self):
        answer = input("Do you want to save container? (y/n): ")
        if answer.lower() in ['y', 'yes']:
            self._container_class.save()

    def switch(self, args = None):
        if self._container_class:
            self._ask_for_save()

        username = input("Enter new username: ")
        self._container_class = UniqueContainer(username)

        self._ask_for_load()

    def _ask_for_load(self):
        pass
    