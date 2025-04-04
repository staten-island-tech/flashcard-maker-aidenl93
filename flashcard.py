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
    def save(self):
        with open ("flashcards.json", 'w') as file:
            json.dump(self.ok, file, indent=4)
while True:
    yaw = input("1 for teacher 2 for student 3 to quit")

    if yaw == "1":
        bro = teach()
        bro.adding()
        bro.show()
        saver = input("wanna save")
        if saver.lower() == "yes":
            bro.save()
            print("saved")  
    elif yaw == "2":
        print("wait")
    elif yaw == "3":
        print("ok")
        break