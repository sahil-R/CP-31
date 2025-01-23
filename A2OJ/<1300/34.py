pages=int(input())
capacity=list(map(int,input().split()))
i=0
while pages>0:
    if pages-capacity[i%7]<=0:
        print(i%7+1)
    pages-=capacity[i%7]
    i+=1