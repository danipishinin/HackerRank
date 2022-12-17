# Occupations

[Pivot](https://en.wikipedia.org/wiki/Pivot_table) the Occupation column in **OCCUPATIONS** so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

**Note**: Print **NULL** when there are no more names corresponding to an occupation.

### Input Format

The **OCCUPATIONS** table is described as follows:

![](https://s3.amazonaws.com/hr-challenge-images/12889/1443816414-2a465532e7-1.png)

Occupation will only contain one of the following values: **Doctor, Professor, Singer** or **Actor**.

### Sample Input

![](https://s3.amazonaws.com/hr-challenge-images/12890/1443817648-1b2b8add45-2.png)

### Sample Output

~~~sql
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
~~~

### Explanation

The first column is an alphabetically ordered list of Doctor names.
The second column is an alphabetically ordered list of Professor names.
The third column is an alphabetically ordered list of Singer names.
The fourth column is an alphabetically ordered list of Actor names.
The empty cell data for columns with less than the maximum number of names per occupation (in this case, the Professor and Actor columns) are filled with **NULL** values.

### Submission:

[occupations.sql](https://github.com/danipishinin/HackerRank/blob/main/sql/occupations.sql)