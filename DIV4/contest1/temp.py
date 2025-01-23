from typing import *

def recruse(index,temp,nums):
    print(index,temp,nums)
    if index==len(nums) and temp==0:
        return True
    elif index<len(nums):
        a=False
        b=False
        if nums[index]<=temp:
            a=recruse(index+1,temp-nums[index],nums)
            if a:
                return True
        b=recruse(index+1,temp,nums)
        if b:
            return True
        return False
    else:
        return False

def isSubsetPresent(n:int, k: int, a: List[int]) -> bool:
    # Write your code here.
    ans= recruse(0,k,a)
    print(ans)

(n,b)=list(map(int,input().split()))
a=list(map(int,input().split()))
print(isSubsetPresent(n,b,a))