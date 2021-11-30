def dogwalker():
    n,k = map(int,input().split(" "))
    arr = []
    for i in range (n):
        arr.append(int(input()))
    arr.sort()
    diff_arr = [arr[i] - arr[i-1] for i in range(1,n)]
    diff_arr.sort(reverse = True)
    return(arr[n-1] - arr[0] - sum(diff_arr[ : k-1]))

if __name__ == '__main__':
    T = int(input())
    while T:
        print(dogwalker())
        T -= 1
