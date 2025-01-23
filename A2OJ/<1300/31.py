# k(n+1)+1=D
n=int(input())
fingers=list(map(int,input().split()))
total=sum(fingers)
c=0
count=1
while total>count:
    count+=(n+1)
# print(count)
for i in range(1,6):
    # print((i+total))
    # print((i+total)-(count))
    if ((i+total)-(count))%(n+1)==0:
        c+=1

print(5-c)