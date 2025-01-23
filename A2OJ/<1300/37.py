(n,k)=list(map(int,input().split()))
if n%2==0:
    odd=n//2
    even=n-odd
else:
    odd=(n//2)+1 
    even=n-odd

if k<=odd:
    ans=k*2-1
else:
    k-=odd
    ans=k*2
print(ans)
