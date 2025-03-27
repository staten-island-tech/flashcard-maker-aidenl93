import json 
class teach: 
    mydict = {}
    wanna = input("wanna make a key? y/n")
    while wanna.lower == "y":
        key = input("give me key")
        value = input ("give me value")
        mydict[key] = value 
        print(mydict)
        
    