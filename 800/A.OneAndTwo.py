t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    # prod=1
    # for i in arr:
    #     prod*=i
    # prod2=1
    # flag=-1
    # for i in range(n):
    #     prod2*=arr[i]
    #     # print(prod2,prod)
    #     if prod2*prod2==prod:
    #         flag=i
    #         break
    # if flag==-1:
    #     print(-1)
    # else:
    #     print(flag+1)
    count2=0
    for i in arr:
        if i==2:
            count2+=1
    if count2%2==1:
        print(-1)
        continue
    temp=0
    if count2==0:
        print(1)
        continue
    for i in range(n):
        if arr[i]==2:
            temp+=1
            if temp==count2//2:
                print(i+1)
                break
    
