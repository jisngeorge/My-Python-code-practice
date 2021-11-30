a = int(input("Enter the number: "))
r = 0
c = 0
while(a!=0) :
    r = (a%2)*(10**c) + r
    a = a//2
    c = c + 1
print(r)
