def plusMinus(arr):
    total = len(arr)
    pos_count = 0
    neg_count = 0
    neutral =0
    for i in arr:
        if i > 0:
            pos_count += 1
        elif i < 0:
            neg_count += 1
        else:
            neutral += 1
    positive = pos_count/total
    negative = neg_count/total
    neutral = neutral/total

    return f"{positive:.6f} \n{negative:.6f} \n{neutral:.6f}"

arr = [1,2,0,-1,-2]
print(plusMinus(arr))