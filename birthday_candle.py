def birthdaycandles(candles):
    maxi = 0
    high = max(candles)
    for i in range(len(candles)):
        if candles[i] == high:
            maxi += 1
    return maxi

candles = [2,3,4,5,5]
print(birthdaycandles(candles))