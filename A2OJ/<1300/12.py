# a=int(input(),2)
# b=int(input(),2)
# print(bin(a^b)[2:])
a=input()
b=input()
s=""
for i in range(len(a)):
    if a[i]==b[i]:
        s+="0"
    else:
        s+="1"
print(s)