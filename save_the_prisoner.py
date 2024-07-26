def saveThePrisoner(n, m, s):
    # Write your code here

    res = s + m -1
    res %= n
    if res == 0:
        return n
    return res

print(saveThePrisoner(5,2,1))

# n - no of prisoners
# m - no of sweets
# s - start of seat number
