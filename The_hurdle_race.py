def hurdleRace(k, height):
    maxnum = max(height)

    if maxnum - k <= 0:
        return 0
    else:
        return maxnum - k

print(hurdleRace(4, [1,6,3,5,2]))