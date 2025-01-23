n=int(input())
scores=list(map(int,input().split()))
max=scores[0]
min=scores[0]
count=0
for i in scores[1:]:
    if i>max:
        count+=1
        max=i
    if i <min:
        count+=1
        min=i
print(count)