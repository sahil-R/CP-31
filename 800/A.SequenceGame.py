t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    ans=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]>=arr[i-1]:
            ans.append(arr[i])
        else:
            ans.append(1)
            ans.append(arr[i])
    print(len(ans))
    for i in ans:
        print(i,end=" ")
    print()