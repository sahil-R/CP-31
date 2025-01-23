t=int(input())
for test in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    if numbers[-1]<len(numbers)-1:
        print(-1)
    else:
        count=0
        flag=0
        for i in range(n-2,-1,-1):
            if numbers[i+1]==0:
                flag=1
                continue
            while numbers[i]>=numbers[i+1]:
                count+=1
                numbers[i]=numbers[i]//2
        if flag:
            print(-1)
        else:
            print(count)