a = input("Enter the string: ")
for i in a:
    if(i.isupper()):
        print(i.lower(),end="")
    else:
        print(i.upper(),end="")
