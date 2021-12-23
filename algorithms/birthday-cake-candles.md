# Birthday Cake Candles

You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

### Example

**candles = [4,4,1,3]**

The maximum height candles are **4**  units high. There are **2** of them, so return **2**.

### Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):

- int candles[n]: the candle heights

### Returns

- int: the number of candles that are tallest

### Input Format

The first line contains a single integer, ***n***, the size of ***candles[]***. The second line contains ***n*** space-separated integers, where each integer **i** describes the height of ***candles[i]***.

### Constraints

- 1 <= n <= 10^5
- 1 <= candles[i] <= 10^7

### Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

### Sample Input

~~~python3
4
3 2 1 3
~~~

### Sample Output

~~~python3
2
~~~

### Explanation

Candle heights are **[3,2,1,3]**. The tallest candles are **3** units, and there are **2** of them.

## Submission:

[mini-max-sum.py](https://github.com/danipishinin/HackerRank/blob/main/algorithms/birthday-cake-candles.py)
