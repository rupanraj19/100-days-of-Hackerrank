def birthday(s, d, m):
    i = 0
    j = m
    count = 0
    
    while j<= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    return count

s = [2,2,1,3,2]
d = 4
m = 2

print(birthday(s, d, m))

#problem
"""
d is the sum value
m is the interval / index
s is the array 

"""
