import math
n=int(input())
arr=list(map(int,input().split()))

minimum=math.inf
l=-1
r=-1
for i in range(n-1):
    if abs(arr[i+1]-arr[i])<minimum:
        l=i
        r=i+1
        minimum=abs(arr[i+1]-arr[i])
i=n-1
if abs(arr[0]-arr[i])<minimum:
    l=0
    r=i
    minimum=abs(arr[0]-arr[i])
print(l+1,r+1)