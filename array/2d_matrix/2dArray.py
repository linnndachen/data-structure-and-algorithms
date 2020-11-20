"""
From Hacker Rank:

> Function Description
hourglassSum has the following parameter(s):
int arr[6][6]: an array of integers

> Return
int: the maximum hourglass sum

>Input Format
Each of the  lines of inputs  contains  space-separated integers .

> Constraints:
- -9 <= arr[i][j] <= 9
- 0 <= i, j<=5

> Output Format
Print the largest (maximum) hourglass sum found in .

> Sample Input
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

>Sample Output
19
"""

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum = []


    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+\
            arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            
    return (max(sum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


"""
further optimization: 
- only store the biggest value until a bigger one replaces it
- currently is N*2 run time. See if we can optimize it.
"""