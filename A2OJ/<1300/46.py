(n,m)=list(map(int,input().split()))
prices=list(map(int,input().split()))

prices=sorted(prices)
# print(prices)
start=0
money=0
for i in range(m):
    if prices[start+i]<=0:
        money-=prices[start+i]
print(money)  
