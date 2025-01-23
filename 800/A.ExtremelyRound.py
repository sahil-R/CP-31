t=int(input())
for i in range(t):
    n=int(input())
    count=0
    base=10
    increment=10
    tmp=100
    if n<base:
        print(n)
    else:
        count+=9
        while base<=n:
            if base<=tmp:
                base=base+increment
                count+=1
            if base>=tmp:
                base=tmp
                tmp=tmp*10
                increment=increment*10
        print(count)
