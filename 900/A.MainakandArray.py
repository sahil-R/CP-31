t=int(input())
for test in range(t):
    n=int(input())
    numbers=list(map(int,input().split( )))
    current_max=numbers[n-1]-numbers[0]
    for i in range(0,n-1):
        # print(numbers[i],numbers[i+1])
        current_max=max(current_max,numbers[i]-numbers[i+1])
    for i in range(1,n-1):
        # print(numbers[i],numbers[i+1])
        current_max=max(current_max,numbers[i]-numbers[0])
    for i in range(0,n-1):
        current_max=max(current_max,numbers[n-1]-numbers[i])
    print(current_max)