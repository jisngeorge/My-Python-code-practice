content = ["This is first line to be written.\n","This is 2nd line\n","End"]
with open("test.txt","w") as file:
    for line in content:
        file.write(line)
with open("test.txt","r") as file:
       print(file.read())

with open("test.txt","a") as file:
    file.write("This is appended content.")

with open("test.txt","r") as file:
       print(file.read())
