def utopianTree(n):
    # Write your code here\
    s = 0

    for i in range(n+1):
        if i%2 == 0:
            s = s + 1
        else:
            s = s * 2
    return s

print(utopianTree(4))

# if even number then add 1 else multiply by 2