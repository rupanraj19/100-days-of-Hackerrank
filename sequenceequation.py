def permutationEquation(p):
    # Write your code here
    x = []
    n = len(p)
    for i in range(1,n+1):
        x.append(p.index(p.index(i)+1)+1)
    return x

print(permutationEquation([2,3,1]))