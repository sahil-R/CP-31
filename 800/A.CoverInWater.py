t=int(input())
for i in range(t):
    n=int(input())
    arr=input()
    if len(arr)<3:
        print(arr.count("."))
    else:
        flag=-1
        for i in range(2,len(arr)):
            if arr[i-2]=="." and arr[i-1]=="." and arr[i]==".":
                flag=2
                break
            else:
                flag=-1
        if flag==2:
            print(2)
        elif flag==1:
            print(1)
        else:
            print(arr.count("."))
    