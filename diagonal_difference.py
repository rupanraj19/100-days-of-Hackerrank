
# import math
# import os
# import random
# import re
# import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
arr = [[1,2,3],[2,3,4],[4,5,10]]

def diagonalDifference(arr):
    # print(arr[0][0] + arr[1][1] + arr[2][2]) #left_to_right
    # print(arr[0][3] + arr[1][1] + arr[3][0]) #right_to_left
    arr_size = len(arr)
    print(arr_size)
    #left to right
    left_to_right = 0
    for i in range(arr_size):
        left_to_right = left_to_right +arr[i][i]
        i += i
        
    #right to left
    right_to_left =0
    for j in range(arr_size):
        right_to_left = right_to_left + arr[j][arr_size-j -1]
        j+=j
    #abs (left to right - right to left)
    return abs(left_to_right - right_to_left)


print(diagonalDifference(arr))