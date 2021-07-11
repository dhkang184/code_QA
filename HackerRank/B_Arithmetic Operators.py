#https://www.hackerrank.com/challenges/python-arithmetic-operators/problem
# 16:00~

# !/bin/python3

import math
import os
import random
import re
import sys


# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_day, t1_dd, t1_Mon, t1_yyyy, t1_t, t1_x = t1.split()
    t2_day, t2_dd, t2_Mon, t2_yyyy, t2_t, t2_x = t2.split()

    t1_time = int(t1_t.split(":")[0]) * 3600 + int(t1_t.split(":")[1]) * 60 + int(t1_t.split(":")[1])
    if int(t1_x) >=0:
        t1_time -= 3600 * int(t1_x[1:3]) + 60 *int(t1_x[3:])
    else:
        t1_time += (3600 * int(t1_x[1:3]) + 60 * int(t1_x[3:]))

    t2_time = int(t2_t.split(":")[0]) * 3600 + int(t2_t.split(":")[1]) * 60 + int(t2_t.split(":")[1])
    if int(t2_x) >=0:
        t2_time -= 3600 * int(t2_x[1:3]) + 60 *int(t2_x[3:])
    else:
        t2_time += (3600 * int(t2_x[1:3]) + 60 * int(t2_x[3:]))
    ans = int(t1_dd) * 24 * 3600 - int(t2_dd)* 24 * 3600 +(t1_time - t2_time)
    return abs(ans)
"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
"""

print(time_delta("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000"))