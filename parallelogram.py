def parallelogram(A, B, C):

    D1 = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    D2 = (A[0] + B[0] - C[0], A[1] + B[1] - C[1])
    D3 = (B[0] + C[0] - A[0], B[1] + C[1] - A[1])

    return(min(D1, D2, D3))

if __name__== "__main__" :
    A = tuple(map(int,input().split(" ")))
    B = tuple(map(int,input().split(" ")))
    C = tuple(map(int,input().split(" ")))

    print(parallelogram(A, B, C))
