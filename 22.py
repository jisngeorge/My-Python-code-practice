#See numbers from 0 -9 of digits of product, the first product that satisfy that condition
n = int(input("Enter the number: "))
digits = set()
i = 1
while(len(digits)!=10):
    a = n*i
    digits.update(list(str(a)))
    i+=1
print(a)
