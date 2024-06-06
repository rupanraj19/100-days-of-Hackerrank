import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    new_grades = []
    for i in grades:
        if i < 38:
            new_grades.append(i)
        elif (math.ceil(i/5)*5 - i) < 3:
            new_grades.append(math.ceil(i/5)*5)
        else:
            new_grades.append(i)
    return new_grades
    
print(gradingStudents([74,43,38,77]))