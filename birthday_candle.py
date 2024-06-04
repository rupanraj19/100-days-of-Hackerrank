def birthdaycandles(candles):
    maxi = 0
    for i in range(len(candles)):
        if candles[i] == max(candles):
            maxi += 1
    return maxi

candles = [2,3,4,5,5]
print(birthdaycandles(candles))