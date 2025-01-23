n=int(input())
x=[i+1 for i in range(n)]
i=1
while i<n:
    temp=x[i]
    x[i]=x[i-1]
    x[i-1]=temp
    i+=2
if n%2==1:
    print(-1)
    exit()
for item in x:
    print(item,end=" ")