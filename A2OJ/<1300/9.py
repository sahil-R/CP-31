number=int(input())
count_lucky=0
while number:
    units=number%10
    number//=10
    if units in [4,7]:
        count_lucky+=1
if count_lucky in [4,7]:
    print("YES")
else:
    print("NO")