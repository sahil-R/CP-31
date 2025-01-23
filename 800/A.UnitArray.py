t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    n_ones=a.count(-1)
    p_ones=a.count(1)
#what i have to satisfy is 2 basic conditions that sum >=0 and product=1
    """for sum to be bigger than 0 we need to have p_ones>n_ones
    and for product to be +ve we need n_ones to be even
    based on this we have 4 conditions that appear
    p_ones>n_ones and n_ones=>even return 0
    p_ones>=n_ones and n_ones=>odd change 1 negative one to positive//return 1
    p_ones<n_ones and n_ones=>even 
    p_ones<n_ones and n_ones=>odd
    if n_ones are more than p_ones then you need to have atleast n/2 number of ones
    as p_ones so that sum becomes 0 thus you need to convert n_ones-n/2 number of ones
    """
    if p_ones>=n_ones and n_ones%2==0:
        print(0)
    elif p_ones>=n_ones and n_ones%2==1:
        print(1)
    else:
        count=0
        # while p_ones<n_ones or n_ones%2==1:
        #     p_ones+=1
        #     n_ones-=1
        #     count+=1
        count=n_ones-n//2
        n_ones=n_ones-count
        if n_ones%2==1:
            count+=1
        print(count)

    
