with open("test.txt","r") as file1:
    content1 = file1.read(5)
    print(content1)
    print("First line: " + file1.readline() )
with open("test.txt","r") as file:
    content = file.readlines()

print(content[1])
