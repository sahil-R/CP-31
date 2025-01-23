
def recurse(index,target,numbers,temp,answer):
    if target==0:
        answer.append(temp.copy())
        return True
    else:
        if index<len(numbers):
            if numbers[index]<=target:
                t1=temp.copy()
                t1.append(numbers[index])
                flag=recurse(index,target-numbers[index],numbers,t1,answer)
                if flag==True:
                    return True
            flag=recurse(index+1,target,numbers,temp,answer)
            if flag==True:
                return True
        else:
            return False
        return False


t=int(input())
for i in range(t):
    (target,n,forbidden)=list(map(int,input().split()))
    numbers=[]
    for i in range(1,n+1):
        if i==forbidden:
            continue
        else:
            numbers.append(i)
    answer=[]
    flag=recurse(0,target,numbers,[],answer)

    # for i in range(len(numbers)-1,-1,-1):
    #     if numbers[i]>target:
    #         continue
    #     else:
    #         quotient=target//numbers[i]
    #         target=target%numbers[i]
    #         for j in range(quotient):
    #             answer.append(numbers[i])
    if not flag:
        print("NO")
    else:
        print("YES")
        answer=answer[0]
        print(len(answer))
        for i in answer:
            print(i,end=" ")
        print()
        