#!/bin/python3

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
    final_grade = []
    for i in range(len(grades)):
        grade = grades[i]
        if(grade % 5 == 0 and grade >= 40):
            final_grade.append(grade)
        else:
            count = 0
            aux = grade
            while(aux % 5 != 0):
                count += 1
                aux += 1
            if(count < 3 and grade >= 37):
                final_grade.append(grade + count)
            else:
                final_grade.append(grade)
    return final_grade
if __name__ == '__main__':
    fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
