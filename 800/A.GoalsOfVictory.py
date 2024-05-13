t=int(input())
for i in range(t):
    n=int(input())
    efficiency=list(map(int,input().split()))
    print(-sum(efficiency))