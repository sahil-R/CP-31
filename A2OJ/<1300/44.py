n=int(input())
score=1
winnner=input()
for _ in range(n-1):
    goal_scored_by_team=input()
    if goal_scored_by_team==winnner:
        score+=1
    else:
        score-=1
        if score==0:
            score=1
            winnner=goal_scored_by_team
print(winnner)