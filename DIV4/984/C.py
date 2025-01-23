t=int(input())
for _ in range(t):
    li=list(input())
    queries=int(input())
    # print(li)
    # print("length:",len(li))
    for j in range(queries):
        (index,binary)=list(map(int,input().split()))
        i=index-1
        if binary==0:
            try:
                if (li[i-3]=="1" and li[i-2]=="1" and li[i-1]=="0") or (li[i-2]=="1" and li[i-1]=="1" and li[i+1]=="0"):
                    print("YES")
            except Exception:
                print("NO")
        elif binary==1:
            try:
                if (li[i+1]=="1" and li[i+2]=="0" and li[i+3]=="0") or (li[i-1]=="1" and li[i+1]=="0" and li[i+2]=="0"):
                    print ("YES")
            except Exception:
                print("NO")
        li[i]=str(binary)
