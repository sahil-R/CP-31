n=int(input())
arr=list(map(int,input().split()))
arr=[abs(x) for x in arr]
print(min(arr))