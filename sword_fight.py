n = int(input())
h = list(map(int, input().split(" ")))
q = int(input())
enimies = n
for j in range(q):
    dead = 0
    x, y = map(int, input().split(" "))
    index = min(n, x)
    for i in range(index):
        if h[i] > 0:
            if (x & i) == i:
                h[i] -= y
                if h[i] < 1:
                    dead += 1
    enimies -= dead
    print(enimies)
