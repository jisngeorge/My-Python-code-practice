'''def sum_subarray(arr, n, k):
    count = 0
    for i in range(n):
        sum_ += arr[j]
        if(sum_ == k):
            count += 1
    return count'''

from collections import defaultdict
def sum_subarray_time(arr, n, k):
    subarray_sum = defaultdict(lambda: 0)
    count = 0
    currSum = 0
    for i in range(n):
        currSum += arr[i]
        if currSum == k:
            count += 1
        if (currSum - k) in subarray_sum:
            count += subarray_sum[currSum - k]
        subarray_sum[currSum] += 1
        print(subarray_sum)
        print(count)
    return count

if __name__ = '__main__':
    n = int(input("N: "))
    arr = list(map(int, input().split(" ")))
    k = int(input("k: "))
    #print(sum_subarray(arr,n,k))
    print(sum_subarray_time(arr,n,k))
