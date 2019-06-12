#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    in_str_count = s[:n].count('a')
    l = len(s)

    if n > l:
        in_str_count *= (n//l)
        if (n % l) != 0:
            in_str_count += s[:n%l].count('a')

    return in_str_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
