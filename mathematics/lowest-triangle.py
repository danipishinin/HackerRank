#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'lowestTriangle' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER trianglebase
#  2. INTEGER area
#

def lowestTriangle(trianglebase, area):
  h = math.ceil(2 * area / trianglebase)
  return h

if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    trianglebase = int(first_multiple_input[0])

    area = int(first_multiple_input[1])

    height = lowestTriangle(trianglebase, area)

    fptr.write(str(height) + '\n')

    fptr.close()
