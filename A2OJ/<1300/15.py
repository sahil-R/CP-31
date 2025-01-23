n=int(input())
li=list(map(int,input().split()))
total=sum([x/100 for x in li])
total=total*100/n
print(f"{total:.12f}")