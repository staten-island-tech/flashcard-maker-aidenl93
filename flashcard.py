import json 
class teach:
    def __init__(self):
        self.ok = {}
    def adding(self):
        while True:
            make = input("give key (or quit by saying quit)")
            if make.lower() == "quit":
                break
            make2 = input("give value")
            self.ok[make] = make2 
    def show(self):
        print(self.ok)

yaw = input("1 for teacher 2 for study")
if yaw == "1":
    bro = teach()
    bro.adding()
    bro.show()
        