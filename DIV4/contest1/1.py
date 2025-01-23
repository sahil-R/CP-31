t=int(input())
for i in range(t):
	(a,b)=list(map(int,input().split()))
	if a>b:
		print(str(b)+" "+str(a))
	else:
		print(str(a)+" "+str(b))
