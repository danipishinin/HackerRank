# Time Conversion

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
- 
### Example

**s = '12:01:00PM'**
  Return '12:01:00'
  
**s = '12:01:00AM'**
  Return '00:01:00'

The maximum height candles are **4**  units high. There are **2** of them, so return **2**.

### Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.
birthdayCakeCandles has the following parameter(s):

timeConversion has the following parameter(s):

- string: the time in **12** hour format 
- 
### Returns

- string: the time in **24** hour format 

### Input Format

A single string ***s*** that represents a time in **12**-hour clock format (i.e.:**hh:mm:ssAM** or **hh:mm:ssPM**).

### Constraints

- All input times are valid

### Sample Input

~~~python3
07:05:45PM
~~~

### Sample Output

~~~python3
19:05:45
~~~

## Submission:

[time-conversion.py](https://github.com/danipishinin/HackerRank/blob/main/algorithms/time-conversion.py)
