def product_one(arr, N):
    steps = 0
    count_zero = 0
    prod = 1
    for i in range(N):
        if(arr[i] > 0):
            steps += (arr[i] - 1)
            prod *= 1
        elif(arr[i] < 0):
            stps += abs(arr[i] + 1)
            prod *= -1
        else:
            count_zero += 1
    steps += count_zero
    if(prod == -1):
        if(count_zero == 0):
            steps += 2
    return steps

if __name__ == '__main__':
    arr = list(map(int, input().split(" ")))
    print(product_one(len(arr)))
    
