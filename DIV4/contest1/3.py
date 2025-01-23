t=int(input())
for i in range(t):
    (a,b,c,d)=list(map(int,input().split()))
    one=set([1,2,3,4,5,6,7,8,9,10,11,12])
    second=set()
    if a>b:
        (a,b)=(b,a)
    for i in range(a,b+1):
        one.remove(i)
        second.add(i)
    if c in one and d in second:
        print("YES")
    elif c in second and d in one:
        print("YES")
    else:
        print("NO")