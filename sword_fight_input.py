def large_n(n, q):
    with open("sword_fight_input.txt", "w") as file:
        file.write(str(n) + "\n")
        for i in range(1, n+1):
            file.write(str(i) + " ")
        file.write("\n" + str(q))
        for k in range(1,q+1):
            file.write("\n" + str(k) + " "+ str(k))

if __name__ == '__main__':
    n, q = map(int,input("Enter n and q separated by spaces: ").split())
    large_n(n, q)
