n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)

team = 0
cur = 0
temp_team = []
while(True):
    if len(array) == 0:
        break
    cur = array.pop()
    temp_team.append(cur)
    
    if len(temp_team) >= cur:
        team += 1
        temp_team = []

print(team)