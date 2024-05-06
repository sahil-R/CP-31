def solution():
    t=int(input())
    for i in range(t):
        n,k=list(map(int,input().split()))
        items=list(map(int,input().split()))
        if k==1:
            asceding=sorted(items)
            if items == asceding:
                print("YES")
            else:
                print("No")
        else:
            print("YES")

if __name__=="__main__":
    solution()