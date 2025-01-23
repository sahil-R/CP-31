t=int(input())
for i in range(t):
    n=int(input())
    a=input()
    rev=a[::-1]
    left=0
    while left<n and a[left]!=rev[left]:
        left+=1
    right=n-1
    while right>0 and a[right]!=rev[right]:
        right-=1
    if left==n and right==0:
        print(0)
    else:
        print(abs(right-left)+1)
