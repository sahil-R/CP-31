t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    end=arr[-1]
    count=arr.count(end)
    c=[end]*count
    for i in range(count):
        arr.remove(end)
    b=arr
    if len(b)==0 or len(c)==0:
        print(-1)
        continue
    print(len(b),len(c),end=" ")
    print()
    for item in b:
        print(item,end=" ")
    print()
    for item in c:
        print(item,end=" ")
    print()
