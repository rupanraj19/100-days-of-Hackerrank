
def bonAppetit(bill, k, b):
    # Write your code here
        total= sum(bill) - bill[k]
        actual = total/2
        if actual == b:
            print('Bon Appetit')
        elif actual < b:
            print(int(b - actual)) 

print(bonAppetit([3,10,2,9],1,7))