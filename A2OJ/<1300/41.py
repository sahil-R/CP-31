(n_houses,n_tasks)=list(map(int,input().split()))
tasks_houses=list(map(int,input().split()))
# tasks_houses=tasks_houses
time_total=tasks_houses[0]-1
# print(time_total)
for i in range(1,n_tasks):
    if tasks_houses[i]>=tasks_houses[i-1]:
        # print(tasks_houses[i]-tasks_houses[i-1])
        time_total+=tasks_houses[i]-tasks_houses[i-1]
    else:
        # print(n_houses-tasks_houses[i])
        time_total+=n_houses-tasks_houses[i-1]
        # print(tasks_houses[i])
        time_total+=tasks_houses[i]
print(time_total)