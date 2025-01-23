n=int(input())
total=0
for _ in range(n):
    s=input()
    if s.count("1")>s.count("0"):
        total+=1
print(total)