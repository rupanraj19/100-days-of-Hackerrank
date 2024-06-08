def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1 # index 
    a[mid], a[n-1] = a[n-1], a[mid]
# [1,2,3,4,5,6,7]
    st = mid + 1 # 4
    ed = n - 2 # 5
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1 #5
        ed = ed - 1 #4 to make while statement false

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)


