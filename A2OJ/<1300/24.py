_1=input()
_2=input()
_3=input()
s1=[0]*26
s2=[0]*26
for _ in _1:
    s1[ord(_)-ord("A")]+=1
for _ in _2:
    s1[ord(_)-ord("A")]+=1
for _ in _3:
    s2[ord(_)-ord("A")]+=1
flag=0
for _ in range(26):
    if s1[_]!=s2[_]:
        flag=1

if flag:
    print("NO")
else:
    print("YES")