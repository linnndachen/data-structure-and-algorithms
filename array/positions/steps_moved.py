
"""
Hacker Ranks - New Year Chaos
> Function Description
Complete the function minimumBribes in the editor below. It must print an integer representing the minimum number of bribes necessary, or Too chaotic if the line configuration is not possible.

> minimumBribes has the following parameter(s):
q: an array of integers

> Input Format
The first line contains an integer , the number of test cases.
Each of the next  pairs of lines are as follows:
- The first line contains an integer , the number of people in the queue
- The second line has  space-separated integers describing the final state of the queue.

> Output Format
Print an integer denoting the minimum number of bribes needed to get the queue into its final state. Print Too chaotic if the state is invalid, i.e. it requires a person to have bribed more than  people.

>Sample Input
2
5
2 1 5 3 4
5
2 5 1 3 4

>Sample Output
3
Too chaotic
"""

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    """
    This was the wrong solution by me. I appraoched from the logic of comparing the ones that took bribe to what they supposed to be. The problem with this is that sometimes a number might be moved due to the numbers in front of it

    The other logic is to comparing the ones that received bribe. Compare from its original position till its current position, how many are bigger than it. 
    res = 0
    q = [P-1 for P in q]
    for i, n in enumerate(q):
        if 3 > (n-i) > 0:
            res+=(n-i)
        elif (n-i)> 2:
            res = 'Too chaotic'
            print (res)
            return
    print (res)
    """

    moves = 0
    Q = [P-1 for P in q]
    for i,P in enumerate(Q):
        if P - i > 2:
            print("Too chaotic")
            return
        for j in range(max(P-1,0),i):
            print(j, P, i)
            if Q[j] > P:
                moves += 1
            print(moves)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)