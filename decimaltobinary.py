import time
n = int(input())

start = time.time()

binary = list()
while n != 0:
    binary.append(n % 2)
    n = n//2
binary.reverse()
print(binary)

end = time.time()

print(start, end, end - start)
#print(binary.reverse()
