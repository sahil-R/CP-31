t=int(input())
#[0,3,6,7,9,45]
#8
"""
mid==6/2=3
find 8 
arr[mid]=7
low=4
2+3=5
high=4

"""
import bisect
def binarysearch(arr,item):
    low=0
    high=len(arr)
    ans=0
    while low<=high:
        mid = low//2+high//2
        if arr[mid]==item:
            return mid
        elif arr[mid]>item:
            high=mid-1
        else:
            ans=mid
            low=mid+1
    return ans

for i in range(t):
    (n,k,q)=list(map(int,input().split()))
    dist=[0]+list(map(int,input().split()))
    time=[0]+list(map(int,input().split()))
    for i in range(q):
        q=int(input())
        index=binarysearch(dist,q)
        if index==len(dist)-1:
            print(time[index],end=" ")
        else:
            speed=(dist[index+1]-dist[index])/(time[index+1]-time[index])
            req=q-dist[index]
            print(time[index]+int(req//speed),end=" ")
    print()
        
