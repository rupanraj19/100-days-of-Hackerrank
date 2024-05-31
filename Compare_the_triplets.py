a= [1,2,3]
b = [4,2,1]

def compareTriplets(a, b):
    # Write your code here
    score_a = 0
    score_b = 0
    # arr = len(a,b)
    for i,j in zip(a,b):
        if i > j:
            score_a += 1
        elif i < j:
            score_b += 1
        else:
            score_a += 0
            score_b += 0
    return [score_a, score_b]
    

print(compareTriplets(a,b))