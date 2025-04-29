import json 
correctans = 0 
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
class student:
    def __init__(self, teach_instance):
        self.teach_instance = teach_instance
    def start(self):
        global correctans
        for key, value in self.teach_instance.ok.items():
            print(key)
            x = input("what is value")
            if x == value:
                print("correct")
                correctans += 1 
                print(f"streak: {correctans}")
            else:
                print(f"wrong lol it was {correctans}")
                correctans = 0 
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
        student_bro = student(bro)
        student_bro.start()
    elif yaw == "3":
        print("ok")
        break