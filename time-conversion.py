import os
import sys

def timeConversion(s): 
    period = s.split(":") 
    # period = [hh, mm, ssAM] || [hh, mm, ssPM]
    hour = period[0]

    if s[-2:] == "PM":
        if hour != "12":
            hour = str(int(hour)+12)
    else:
        if hour == "12":
            hour = "00"
    period[0] = hour
    time = ':'.join(period)
    return str(time[:-2])

if __name__ == '__main__':
    fptr = sys.stdout

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
