def minimaxsum(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]

    print(sum - max(arr), sum - min(arr))

arr = [1,2,3,4,5]
print(minimaxsum(arr))
