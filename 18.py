a = input("Enter first word: "))
b = input("Enter second word: "))
l1 = list(a.lower())
l2 = list(b.lower())
l1.sort()
l2.sort()
if(l1 == l2):
    print("Anagram")
else:
    print("Not Anagram")
