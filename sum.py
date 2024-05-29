arr = [1,2,4]

def simpleArraySum(arr):
    arrsum = 0
    for i in arr:
        arrsum = arrsum + i
        print(arrsum)
    return arrsum
    #return sum(arr) another method
print(simpleArraySum(arr))
    