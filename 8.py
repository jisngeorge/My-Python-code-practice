a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))
'''
if(a>b and a>c):
    print("Greatest is ",a)
    if(b>c):
        print("Second Greatest is",b)
        print("Smallest is ",c)
    else:
        print("Second Greatest is",c)
        print("Smallest is ",b)
elif(b>c):
    print("Greatest is ",b)
    if(a>c):
        print("Second Greatest is ",a)
        print("Smallest is ",c)
    else:
        print("Second Greatest is ",c)
        print("Smallest is ",a)
else:
    print("Greatest is ",c)
    if(a>b):
        print("Second Greatest is ",a)
        print("Smallest is ",b)
    else:
        print("Second Greatest is ",b)
        print("Smallest is",a)
'''
print("Greatest:",max(a,b,c))
print("Second Greatest:",a+b+c - max(a,b,c) - min(a,b,c))
print("Smallest:",min(a,b,c))
