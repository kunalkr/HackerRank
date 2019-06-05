#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pair_count = 0
    color_count_map = dict()

    for sock in ar:
        color_count_map[sock] = color_count_map.get(sock, 0) + 1
    for key, val in color_count_map.items():
        pair_count += (val//2)
    return pair_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

