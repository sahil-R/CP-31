k=int(input())
l=int(input())
m=int(input())
n=int(input())
d=int(input())

li=[0]*(d+1)
for i in [k,l,m,n]:
    j=i
    while j<=d:
        li[j]=1
        j+=i
# print(li)
print(li[1:].count(1))