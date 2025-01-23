t=int(input())
import math
for test in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    if numbers[0]==1:
        numbers[0]+=1
    for i in range(1,n):
        if numbers[i]==1:
            numbers[i]+=1
        if math.gcd(numbers[i],numbers[i-1])==numbers[i-1]:
            numbers[i]+=1
    print(" ".join([str(x) for x in numbers]))