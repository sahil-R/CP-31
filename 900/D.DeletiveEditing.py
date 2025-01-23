t=int(input())
for test in range(t):
    (s,t)=input().split()
    d={}
    if len(t)>len(s):
        print("NO")
        continue
    for iter in range(len(s)):
        if s[iter] not in d:
            d[s[iter]]=[iter]
        else:
            d[s[iter]].append(iter)
    last=None
    flag=0
    for item in range(len(t)):
        letter=t[len(t)-item-1]
        if letter not in d:
            flag=1
            break
        else:
            if last==None:
                matches=d[letter]
            else:
                also_matches=[x for x in d[letter] if x>last]
                if also_matches:
                    flag=1
                    break
                matches=[x for x in d[letter] if x < last]
            if matches:
                last=max(matches)
            else:
                flag=1
                break
            if last in d[letter]:
                d[letter].remove(last)
            else:
                flag=1
                break
            # print(last)
    if flag:
        print("NO")
    else:
        print("YES")