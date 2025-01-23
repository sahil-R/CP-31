n=int(input())
growth=list(map(int,input().split()))

growth=sorted(growth,reverse=True)
print(growth)
start=0
while n>0:
    n-=growth[start]
    start+=1
    # print(start)
    if start==len(growth)-1 and n>=0:
        start=-1
        break
print(start)