chars=[0]*26
s=input()
for _ in s:
    chars[ord(_)- ord("a")]=1

if sum(chars)%2==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")