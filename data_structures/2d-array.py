#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    maxSum = -99999
    
    for i in range(4):
        for j in range(4):

            topSum = sum(arr[i][j:j+3])

            midSum = arr[i+1][j+1]
            
            bottomSum = sum(arr[i+2][j:j+3])
            
            total = topSum + midSum + bottomSum
            
            if total > maxSum:
                maxSum = total
    return maxSum        
          
if __name__ == '__main__':
    fptr = sys.stdout

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
