from typing import *

def maximumWeightRow(n: int, m: int, mat: List[List[int]]) -> int:
    # Write your code here.
    #initialize max value to min value
    max = -1
    for i in range(n):# for every row
        sum = 0
        for j in range(m):#for every col
            sum+=mat[i][j]
            if sum>max:
                max = sum
    return max
