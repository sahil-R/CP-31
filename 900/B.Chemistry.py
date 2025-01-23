t=int(input())
for i in range(t):
    (n,k)=list(map(int,input().split()))
    s=input()
    count=0
    d=[0]*26
    for i in s:
        if d[ord(i)-ord('a')]!=0:
            d[ord(i)-ord('a')]+=1
        else:
            d[ord(i)-ord('a')]=1
    
    for value in d:
        if value%2==1:
            count+=1
    
    if count-1<=k or len(s)==1:
        print("YES")
    else:
        print("NO")