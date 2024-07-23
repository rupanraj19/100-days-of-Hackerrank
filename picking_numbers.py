# counter to count the number of occurrences of the number.
# then compare them with the next number in the array and find the max length

from collections import Counter
def pickingNumbers(a):
    arr = Counter(a)
    maxnum = 0

    for i in range(100):
        maxnum = max(maxnum, arr[i]+arr[i+1])

    return maxnum

print(pickingNumbers([4, 6, 5, 3, 3, 1]))