def median(arr):
    arr.sort()
    mid = len(arr)//2
    if(len(arr)%2)==0:
        return (arr[mid-1] + arr[mid]) /2
    else:
        return arr[mid]

print(median([2,4,5,1]))