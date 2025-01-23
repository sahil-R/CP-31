t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    item=max(arr)
    x=[str(item+1-y) for y in arr]
    print(" ".join(x))