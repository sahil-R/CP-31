n=int(input())
x=0
for _ in range(n):
    s=input()
    if s=="X++" or s=="++X":
        x+=1
    elif s=="X--" or s=="--X":
        x-=1
    else:
        x+=0
print(x)
