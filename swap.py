N = int(input("Enter the length of array: "))
M = int(input("Enter the number of swaps: "))
A = []
for i in range(0, N):
    A.append(i+1)

def swp(A,N):
    S = []
    for i in range(0, N):
        j = i + 1;
        while j < N:
            B = A[:]
            temp = B[j]
            B[j] = B[i]
            B[i] = temp
            S.append(B)
            j = j + 1
    return S

W = [A]
V = []
while M > 0:
    for i in W:
        for j in swp(i,N):
            if j not in V:
                V.append(j)
    W = V[:]
    V = []
    M = M - 1;

print("Number of unique arrays: ",len(W))
