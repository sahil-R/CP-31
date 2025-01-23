s=input()
_s=input()
start=0
end=len(s)-1
if len(s)!=len(_s):
    print("NO")
else:
    while start!=len(s):
        if s[start]!=_s[end]:
            print("NO")
            exit()
        start+=1
        end-=1
    print("YES")
    exit()