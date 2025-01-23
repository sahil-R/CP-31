t=int(input())
for test in range(t):
    n=int(input())
    i=1
    while True:
        if n%i!=0:
            print(i-1)
            break
        i+=1
    