year=int(input())
for i in range(year+1,15000):
    s=set(str(i))
    if len(s)==4:
        print(i)
        break