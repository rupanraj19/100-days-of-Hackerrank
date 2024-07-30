def beautifulDays(i, j, k):
    # Write your code here
    count = 0
    for i in range(i,j+1):
        rx = int(str(i)[::-1])

        if abs(i - rx)%k == 0:
            count += 1

    return count

print(beautifulDays(20,23,6))

"""
    jus need to find which day is good to go as it is perfectly divisible by k and find the difference of number to the start day number
    i - reverse(i) % k == 0t
    then increase count by 1
    return count
"""