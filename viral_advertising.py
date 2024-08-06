import math
def viralAdvertising(n):
    result = 0
    people = 5
    x = 0
    for i in range(n):
        d = math.floor(people/2) # can use //
        x += d
        people = d * 3
    return x

print(viralAdvertising(3))