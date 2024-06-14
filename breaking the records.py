def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score = scores[0]
    max_count = 0
    min_count = 0
    for i in scores:
        if i > max_score:
            max_score = i
            max_count += 1
        elif i < min_score:
            min_score = i
            min_count += 1
    return max_count, min_count

print(breakingRecords([10,5,20,20,4,5,2,25,1]))