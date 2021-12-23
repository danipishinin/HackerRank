import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    maior = max(arr)
    menor = min(arr)
    soma = sum(arr)
    minimumSum = soma - maior
    maximumSum = soma - menor
    print(minimumSum,maximumSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
