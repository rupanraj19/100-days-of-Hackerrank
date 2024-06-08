def lonelyinteger(a):
    counts = {} #create dictionary to track key and value

    for i in a:
        if i in counts:
            counts[i] = counts[i] + 1 #if i inside dict add 1
        else:
            counts[i] = 1 #if i is not inside then create key and value =1

    for key,value in counts.items():
        if value == 1:
            return key
        

print(lonelyinteger([1,2,3,3,3,2]))