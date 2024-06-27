from collections import Counter
def sockMerchant(n, ar):
    # Write your code here
    count = Counter(ar)
    pairs = 0
    for i in count:
        pairs += count[i] //2 
    return pairs

print(sockMerchant(5, [1,2,3,2,1]))