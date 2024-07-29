def angryProfessor(k, a):
    # Write your code here
    count = 0

    for i in a:
        if i <= 0:
            count += 1
    if count < k:
        return "YES"
    else:
        return "NO"


print(angryProfessor(2,[-1,0,0,1]))

# angry prof want to start class only if he get the certain no of students before the time. if they late and got less number return "yes" to cancel else "no" to cancel