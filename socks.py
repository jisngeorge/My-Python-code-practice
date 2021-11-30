n = int(input())
s = input()

socks = list()
colours = list()
number = list()
colour = set()

socks = s.split()

for sock in socks:
    c = int(sock)
    colours.append(c)
    colour.add(c)

for c in colour:
    number.append(colours.count(c))

for i in range(len(number)):
    number[i] = number[i]//2

pair = sum(number)

print(pair)
