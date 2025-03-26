class user:
    def __init__(self,name,email):
        self.name = name 
        self.email = email 

    def displayinfo(self):
        return f"user: {self.name}, {self.email}"

bro = user("aiden","email")
print(bro)