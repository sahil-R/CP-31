t=int(input())

for i in range(t):
    n=int(input())
    flag=False
    temp=n+1
    temp2=n-1
    if temp%3==0 or temp2%3==0:
        print("First")
        flag=True
    if flag==False:
        print("Second")