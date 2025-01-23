n=int(input())
s=input()
count=0
for _ in range(1,n):
    if s[_-1]==s[_]:
        count+=1
print(count)