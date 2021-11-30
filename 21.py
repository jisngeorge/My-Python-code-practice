#Decimal to binary recursive
d = int(input("Enter the number: "))

def binary (a) :
    if a > 1 :
        binary(a//2)
    print(a%2,end = "")


binary(d)
