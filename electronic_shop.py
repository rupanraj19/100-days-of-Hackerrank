def getMoneySpent(keyboards, drives, b):
    
    maxamount = -1
    
    for i in keyboards:
        for j in drives:
            if (i+j) <= b:
                maxamount = max(maxamount, i+j)
    return maxamount


print(getMoneySpent([5,1,1],[1],1))

