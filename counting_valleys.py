def countingValleys(steps, path):
    # Write your code here
    count  = 0
    result = 0
    for i in range(len(path)):
        if path[i] == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and  path[i] == 'U':
            result += 1
    return result

print(countingValleys(8, ['U','D','D','D','U','D','U','U']))

# count the meeting point in the sea level 
# find which path it comes from if U means valley (down to up)
#  vice versa
# if the count == 0 and path[0] == 'U': then add the result + 1
# this is our valley couting