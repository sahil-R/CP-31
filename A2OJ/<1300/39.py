_zero=0
_one=0
_two=1
li=[]
li.append(_zero)
li.append(_one)
li.append(_two)
n=int(input())
while True:
    new=_two+_one
    li.append(new)
    if new >= n:
        break
    _zero=_one
    _one=_two
    _two=new
if n in li:
    print(n,0,0)
else:
    print("I'm too stupid to solve this problem")