def kangaroo(x1, v1, x2, v2):
    # Write your code here
    h = x2-x1 #(distance)
    
    if v1 > v2 and h%(v1-v2) ==0: #to be yes, velocity 1 must be greater than v2 and use distance to find the meeting point
        return 'YES'
    else:
        return 'NO'

print(kangaroo(0,3,2,2))
