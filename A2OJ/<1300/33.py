n=int(input())
x=[]
y=[]
points=[]
for i in range (n):
    (tx,ty)=list(map(int,input().split()))
    #x.append()
    points.append((tx,ty))
p=0
for i in range(n):
    a=0;b=0;c=0;d=0
    for j in range(n):
        if points[i][0]==points[j][0]:
            if points[i][1]>points[j][1]:
                a+=1
            if points[i][1]<points[j][1]:
                b+=1
        elif points[i][1]==points[j][1]:
            if points[i][0]>points[j][0]:
                c+=1
            if points[i][0]<points[j][0]:
                d+=1
    if a>=1 and b>=1 and c>=1 and d>=1:
        p+=1

print(p)
