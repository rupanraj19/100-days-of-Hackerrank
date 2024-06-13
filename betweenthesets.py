def getTotalX(a, b):
    count = 0
    for i in range(max(a), min(b) + 1):
        is_multiple_of_a = True
        for x in a:
            if i % x != 0:
                is_multiple_of_a = False
                break
        if is_multiple_of_a:
            is_factor_of_b = True
            for x in b:
                if x % i != 0:
                    is_factor_of_b = False
                    break
            if is_factor_of_b:
                count += 1
    return count

a = [2, 4]
b = [12, 24]
print(getTotalX(a, b))  # Output: 2

a = [3, 6]
b = [18, 36]
print(getTotalX(a, b))  # Output: 1

#first array - lcm
#second array - gcd

#return In other words, it's finding the number of integers that are multiples of the LCM of the first array and also divide the GCD of the second array.