
# Find Point

Consider two points **p = (p<sub>x</sub>,p<sub>y</sub>) and q = (q<sub>x</sub>,q<sub>y</sub>)** We consider the inversion or [point reflection](https://en.wikipedia.org/wiki/Point_reflection), **r = (r<sub>x</sub>,r<sub>y</sub>)**, of point **p** across point **q** to be a **180°** rotation of point **p** around **q**.

Given **n** sets of points **p** and **q**, find **r** for each pair of points and print two space-separated integers denoting the respective values of **r<sub>x</sub>** and **r<sub>y</sub>** on a new line.

### Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

- int px, py, qx, qy: x and y coordinates for points **p** and **q**

### Returns

- int[2]: x and y coordinates of the reflected point **r**

### Input Format

The first line contains an integer,**n**, denoting the number of sets of points.
Each of the **n** subsequent lines contains four space-separated integers that describe the respective values of **p<sub>x</sub>**,**p<sub>y</sub>**, **q<sub>x</sub>**, and **q<sub>y</sub>** defining points **p = (p<sub>x</sub>,p<sub>y</sub>) and q = (q<sub>x</sub>,q<sub>y</sub>)**

### Constraints

- 1 <= n <= 15

- -100 <= **p<sub>x</sub>**,**p<sub>y</sub>**, **q<sub>x</sub>**, **q<sub>y</sub>** <= 100

### Sample Input

~~~python
2
0 0 1 1
1 1 2 2
~~~

### Sample Output

~~~python
2 2
3 3
~~~

### Explanation

The graphs below depict points **p**,**q**, and **r**  for the **n = 2** points given as Sample Input:

![](https://s3.amazonaws.com/hr-challenge-images/128/1476208076-15f0f71f16-find-point-0011.png)

![](https://s3.amazonaws.com/hr-challenge-images/128/1476207535-debed1b871-find-point-1122.png)

## Submission:

[find-point.py](https://github.com/danipishinin/HackerRank/blob/main/mathematics/find-point.py)
