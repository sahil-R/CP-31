t=int(input())
import math
for test in range(t):
    n=int(input())
    # if n%4!=0 and n%6!=0 and n%12!=0:
    if n&1==1 or n<4:
        print(-1)
        continue
    else:
        x=n//2
        max=(x//2)
        if x%3==0:
            min=x//3
        else:
            min=x//3+1
        print(str(min)+" "+str(max))
