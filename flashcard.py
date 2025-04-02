import json 
class teach:
    def __init__(self):
        self.store = {}
    def addpair(self, key, value):
        self.store[key] = value 
    def getvalue(self,key):
        return self.store.get(self, key)
    def display(self):
        for key, value in self.store.items():
            print(f"ok {key} {value}")