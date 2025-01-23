import math
n=int(input())
li=list(map(int,input().split()))
maxi=-math.inf
max_index=-1
mini=math.inf
min_index=-1
for i in range(n):
    if li[i]>maxi:
        maxi=li[i]
        max_index=i
for i in range(n-1,-1,-1):
    if li[i]<mini:
        mini=li[i]
        min_index=i
# print(min_index)
if min_index<max_index:
    min_index+=1
# print(max_index,min_index)
print(max_index+n-1-min_index)