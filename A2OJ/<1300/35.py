
(a,b,c)=list(map(int,input().split()))

_ABC=(a*b*c)**0.5
print(round(4*(_ABC)*(1/a+1/b+1/c)))