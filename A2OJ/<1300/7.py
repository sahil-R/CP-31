s=input()
# print(ord("A"))
# print(ord("Z"))
# print(ord("a"))
# print(ord("z"))
capital=0
lower=0

for i in s :
    if ord(i)>=65 and ord(i)<=90:
        capital+=1
    else:
        lower+=1

if lower>=capital:
    print(s.lower())
else:
    print(s.upper())