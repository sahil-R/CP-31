n=int(input())
_fives=0
_zeros=0
numbers=list(map(int,input().split()))
for i in numbers:
    if i==5:
        _fives+=1
    else:
        _zeros+=1

# print(_zeros,_fives)
if _zeros==0:
    print(-1)
else:
    print(int('5'*(((_fives)//9)*9)+'0'*_zeros))