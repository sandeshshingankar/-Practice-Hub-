#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY cost
#  2. STRING_ARRAY labels
#  3. INTEGER dailyCount
#

def maxCost(cost, labels, dailyCount):
    left = 0
    legal_count = 0
    current_cost = 0
    max_cost = 0
    
    for right in range(len(cost)):
        current_cost += cost[right]
        
        if labels[right] == "legal":
            legal_count += 1
        
        while legal_count > dailyCount:
            current_cost -= cost[left]
            if labels[left] == "legal":
                legal_count -= 1
            left += 1
        
        if legal_count == dailyCount:
            max_cost = max(max_cost, current_cost)
    
    return max_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cost_count = int(input().strip())
    cost = []

    for _ in range(cost_count):
        cost_item = int(input().strip())
        cost.append(cost_item)

    labels_count = int(input().strip())
    labels = []

    for _ in range(labels_count):
        labels_item = input().strip()
        labels.append(labels_item)

    dailyCount = int(input().strip())

    result = maxCost(cost, labels, dailyCount)

    fptr.write(str(result) + '\n')
    fptr.close()
