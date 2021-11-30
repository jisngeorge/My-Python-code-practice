t = int(input())
for i in range(t):
    p, c = map(int,input().split(" "))
    output = ""
    pj = list(map(int,input().split(" ")))
    for j in pj:
        if(c >= j):
            output += '1'
            c -= j
        else:
            output += '0'
    print(output)
