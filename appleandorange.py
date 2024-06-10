def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    count_apples = 0
    count_orange = 0
    
    for i in apples:
        if i + a in range(s,t+1):
            count_apples += 1
    for j in oranges:
        if j + b in range(s,t+1):
            count_orange += 1
    print(count_apples, count_orange,sep="\n")
            
# 7 11
# 5 15
# 3 2
# -2 2 1
# 5 -6
print(countApplesAndOranges(7,11, 5, 15, [3,2,-2], [2,1,5,-6]))