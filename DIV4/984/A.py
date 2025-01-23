t=int(input())
for _ in range(t):
    n = int(input())
    flag=0
    numbers=list(map(int,input().split()))
    for i in range(1,n):
        if flag==1:
            break
        if abs(numbers[i]-numbers[i-1]) not in [5,7]:
            flag=1
    if flag==1:
        print("NO")
    else:
        print("YES")