t=int(input())
for test in range(t):
    (n,d)=list(map(int,input().split()))
    numbers=list(map(int,input().split()))
    total=0
    maxcount=1
    numbers=sorted(numbers)
    # print(numbers)
    current=numbers[0]
    if n==1:
        print(0)
    else:
        for i in numbers[1:]:
            if i-current<=d:
                maxcount+=1
                current=i
                total=max(total,maxcount)
                # print(current,total)
            else:
                current=i
                maxcount=1
        total=max(total,maxcount)
        # print(total)
        print(n-total)
    # print("-------------")

