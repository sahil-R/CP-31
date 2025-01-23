(x,y)=list(map(int,input().split()))
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
np=-1
for item in primes[::-1]:
    if item>x:
        np=item

if y==np:
    print("YES")
else:
    print("NO")