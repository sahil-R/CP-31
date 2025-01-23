t=int(input())
for test in range(t):
    n=int(input())
    answers=input()
    options=set(['A','B','C','D'])
    total=0
    for i in options:
        total+=min(n,answers.count(i))
    print(total)