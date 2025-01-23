t=int(input())
for _ in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    d={}
    m=0
    for i in numbers:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
        m=max(m,d[i])
    count=0
    value=m
    while value<n:
        count+=1 
        if 2*value>n:
            count+=n-value
            break
        else:
            count+=value
            value=2*value
    print(count)

    