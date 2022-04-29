# Bot saves princess - 2

In this version of "Bot saves princess", Princess Peach and bot's position are randomly set. Can you save the princess?

### Task

Complete the function nextMove which takes in 4 parameters - an integer N, integers r and c indicating the row & column position of the bot and the character array grid - and outputs the next move the bot makes to rescue the princess.

## Input format

The first line of the input is N (<100), the size of the board (NxN). The second line of the input contains two space separated integers, which is the position of the bot.

Grid is indexed using [Matrix Convention](https://www.hackerrank.com/scoring/board-convention)

The position of the princess is indicated by the character 'p' and the position of the bot is indicated by the character 'm' and each cell is denoted by '-' (ascii value: 45).

## Output format

Output only the **next** move you take to rescue the princess. Valid moves are LEFT, RIGHT, UP or DOWN

## Sample input

~~~py 
5
2 3
-----
-----
p--m-
-----
-----
~~~

### Sample output

~~~py
LEFT
~~~

### Resultant State

~~~py
-----
-----
p-m--
-----
-----
~~~

### Explanation

As you can see, bot is one step closer to the princess.

### Scoring

Your score for every testcase would be (NxN minus number of moves made to rescue the princess)/10 where N is the size of the grid (5x5 in the sample testcase). Maximum score is 17.5

## Submission:

[bot-saves-princess2.py](https://github.com/danipishinin/HackerRank/blob/main/artificial_intelligence/bot-saves-princess2.py)
