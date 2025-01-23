t=int(input())
for test in range(t):
    n=int(input())
    s=list(input())
    length=1
    temp=1
    for i in range(1,n):
        if s[i]==s[i-1]:
            temp+=1
            length=max(length,temp)
        else:
            temp=1
    print((length+1))