s=input()
borz={
    ".":0,
    "-.":1,
    "--":2
}
i=0
ops=""
while i <len(s)-1:
    if s[i]==".":
        ops+="0"
    else:
        if s[i+1]==".":
            ops+="1"
        else:
            ops+="2"
        i+=1
    i+=1
if i<len(s) and s[-1]==".":
    ops+="0"

print(ops)