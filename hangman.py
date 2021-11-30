print("HANGMAN")
n = input("Enter the name: ").lower()
k = len(n)
n1 = list(n)
l1 = ["_" for i in range(k)]
while k != 0 :
    l = input("Enter the letter: ").lower()
    if l in n1:
        print("Correct!!!")
        p = n1.index(l)
        l1[p] = l
        n1[p] = None
        print(l1)
    else:
        k = k - 1
        print("Incorrect!!! You have",k,"chances.")
        print(l1)
    if '_' not in l1 and None in n1 :
        print("Won!!!\n",l1)
        break
if k == 0:
    print("You Lose")
