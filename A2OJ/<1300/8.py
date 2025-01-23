s=input()
s=list(s)
if s[0]==s[0].lower():
    s[0]=s[0].upper()
print("".join(s))