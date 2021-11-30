with open("test.txt","w") as file:
    file.write("This file has been modified!")
with open("test.txt","r") as file:
    print(file.read())
with open("test.txt","w") as file:
    file.write("This file is last modified @ 10:18 PM\n")
    file.write("This file is last modified @ 10:19 PM")
with open("test.txt","r") as file:
    print(file.read())
