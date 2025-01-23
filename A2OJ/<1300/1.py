t=int(input())
tx=0;ty=0;tz=0
for _ in range(t):
    (x,y,z)=list(map(int,input().split()))
    tx+=x;ty+=y;tz+=z
if not tx and not ty and not tz:
    print("YES")
else:
    print("NO")