(n,k,l,c,d,p,nl,np)=list(map(int,input().split()))
total_drink=k*l
total_slices=d*c
print(min(total_drink//nl,total_slices,p//np)//n)