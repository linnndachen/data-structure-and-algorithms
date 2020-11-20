"""
Q1: From Hacker Rank
> Function Description:
Complete the function rotLeft in the editor below. It should return the resulting array of integers.
rotLeft has the following parameter(s):
- An array of integers .
- An integer , the number of rotations.

> Input Format
The first line contains two space-separated integers  and , the size of  and the number of left rotations you must perform.
The second line contains  space-separated integers.

>Output Format
Print a single line of  space-separated integers denoting the final state of the array after performing  left rotations.

>Sample Input
5 4
1 2 3 4 5

>Sample Output
5 1 2 3 4
"""

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    return a[d:]+a[:d]
