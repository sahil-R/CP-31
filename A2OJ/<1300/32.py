import math
(n,mx)=list(map(int,input().split()))
numbers=list(map(int,input().split()))
m=-math.inf
mi=-1
for i in range(n):
    numbers[i]=math.ceil(numbers[i]/mx)
for i in range(n-1,-1,-1):
    if numbers[i]>m:
        m=numbers[i]
        mi=i
print(mi+1)