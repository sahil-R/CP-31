t=int(input())
import math
for test in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    odd=[]
    even=[]
    max_odd=-math.inf
    min_even=math.inf
    count_odd=0
    for item in numbers:
        if item%2==0:
            even.append(item)
        else:
            count_odd+=1
            max_odd=max(max_odd,item)
    even=sorted(even)
    c1=0
    c2=0
    temp=max_odd
    i=0
    if len(even)==0 or len(even)==n:
        print(0)
        continue
    # print((even),n)
    if len(even)>count_odd:
        while i<len(even):
            c1+=1
            item=even[i]
            total=item+temp
            if item>temp:
                temp=total
                i-=1
            i+=1
        i=len(even)-1
        while i>=0:
            c2+=1
            item=even[i]
            total=item+temp
            if item>temp:
                temp=total
                i+=1
            i-=1
        print (max(c1,c2))
    else:
        print(count_odd)    