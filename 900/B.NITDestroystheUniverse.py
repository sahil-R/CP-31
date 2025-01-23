t=int(input())
for test in range(t):
    n=int(input())
    numbers=list(map(int,input().split()))
    # numbers=input()
    # numbers=numbers.replace(" ","")
    # x=[item for item in numbers.split('0') if item!='']
    # print(len(x))
    count=0
    left=None
    for item in numbers:
        if item==0:
            left=None
            continue
        else:
            if left==None:
                count+=1
                left=item
    if count in [0,1]:
        print(count)
    else:
        print(2)

    
    