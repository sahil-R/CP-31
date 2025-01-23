t=int(input())
for test in range(t):
    n,t2=list(map(int,input().split()))
    arr=list(map(int,input().split()))
    prefixsum=dict()
    temp=0
    prefixsum[0]=0
    for i in range(n):
        temp+=arr[i]
        prefixsum[i+1]=temp
    total=prefixsum[n]
    for test2 in range(t2):
        l,r,k=list(map(int,input().split()))
        ktotal=(r-l+1)*(k)
        pseudosum=prefixsum[r]-prefixsum[l-1]
        if (total-pseudosum+ktotal)%2==0:
            print("NO")
        else:
            print("YES")
