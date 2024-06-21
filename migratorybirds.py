def migratoryBirds(arr):
    # Write your code here
    b = [0,0,0,0,0,0]
    
    for i in arr:
        b[i] += 1
    return b.index(max(b))
  
print(migratoryBirds([1,2,3,3,3,2,1]))