n=int(input())
town_travel_time=list(map(int,input().split()))

index=0
time=town_travel_time[0]
duptime=[]
for town in range(1,n):
    if town_travel_time[town] == time:
        duptime.append(time)
    elif town_travel_time[town] < time :
        index=town
        time=town_travel_time[town]
# print(time,index)
# print(duptime)
if time in duptime:
    print("Still Rozdil")
else:
    print(index+1)