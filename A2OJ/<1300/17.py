n=int(input())
left_zeros=0
left_ones=0
right_zeros=0
right_ones=0
for _ in range(n):
    (l,r)=list(map(int,input().split()))
    if l==0:
        left_zeros+=1
    else:
        left_ones+=1
    if r==0:
        right_zeros+=1
    else:
        right_ones+=1
print(sum([min(left_zeros,left_ones),min(right_zeros,right_ones)]))