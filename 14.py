a = input("Enter the string: ")
count=0
for i in a:
    if(i in 'AEIOUaeiou'):
        count+=1
print(count)
