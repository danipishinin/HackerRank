import math
import os
import random
import re
import sys

def plusMinus(arr):
    isPositive = 0
    isNegative = 0
    isNeutro = 0
    for i in range(len(arr)):
        if(arr[i] > 0):
            isPositive += 1
        elif(arr[i] < 0):
            isNegative +=1
        else:
            isNeutro += 1
    print(round(isPositive / n, 6))
    print(round(isNegative / n, 6))
    print(round(isNeutro / n, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
