import math
import os
import random
import re
import sys

def birthdayCakeCandles(candles):
    maximum_height = 0
    maximum_candles = 0
    for i in range(candles_count):
        if(candles[i] > maximum_height):
            maximum_height = candles[i]
    for i in range(candles_count):
        if(candles[i] == maximum_height):
            maximum_candles+= 1
    return maximum_candles

if __name__ == '__main__':
    fptr = sys.stdout

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
