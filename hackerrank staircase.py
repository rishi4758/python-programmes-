#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
   list=[];
   print(arr)
   for i in arr:
       print(i,end="  ")
       sum=0;
       for j in arr:
         sum=sum+j;
         print(j,"sdkjd")
       sum=sum-i  
       list.append(sum);
   print(list)
   val=sorted(list)
   print( val[0],val[-1])






if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
