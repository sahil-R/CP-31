t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    if len(set(arr))==1:
        print("NO")
    else:
        print("YES")
        item=arr.pop()
        arr=[item]+arr
        print(" ".join([str(x) for x in arr]))