s=input()
s=s.replace("144", "T")
# print(s)
s=s.replace("14","A")
# print(s)
s=s.replace("1","B")
# print(s)
for item in s:
    if ord(item)-ord('0') in [0,1,2,3,4,5,6,7,8,9]:
        print("NO")
        exit()
print("YES")