t=int(input())
for i in range(t):
    (n,j)=(map(int,input().split()))
    arr=list(map(int,input().split()))
    init=arr[0]
    mid=0
    end=2*(j-arr[-1])
    if len(arr)>1:
        mid=[arr[i]-arr[i-1] for i in range(1,len(arr)) ]
        print(max(init,end,max(mid)))
    else:
      print(max(init,end))