t = int(input())
l = list()
f = []
i = 0
while i < t :
    l.append(int(input()))
    f.append(0)
    while l[i] != 0 :
        if l[i] % 10 == 4:
            f[i] = f[i] + 1
        l[i] = int(l[i] / 10)
    i = i + 1
for q in f:
    print(q,"\n")


