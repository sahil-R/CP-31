import math
t=int(input())
from functools import reduce

def gcd_of_list(num_list):
    return reduce(math.gcd, num_list)
for temp in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    temp=[]
    for i in range(n):
        if abs(numbers[i]-(i+1))>0:
            temp.append(abs(numbers[i]-(i+1)))
    print(gcd_of_list(temp))
