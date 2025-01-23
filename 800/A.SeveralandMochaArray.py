import math
t=int(input())
for i in range(t):
    n=int(input())
    flag=False
    arr=list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if math.gcd(arr[i],arr[j])<=2:
                flag=True
    if flag:
        print("YES")
    else:
        print("NO")
    