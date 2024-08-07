#124 -> check 1,2,4 are the divisors of the 124 that divide it perfectly (remainder = 0) then return the number of perfect divisors
def findDigits(n):
    # Write your code here
    count = 0

    for i in str(n):
        if int(i)!=0 and n%int(i) ==0:
            count += 1
    return count

print(findDigits(124))

#trick is to change number into string so can access the number easily in for loop