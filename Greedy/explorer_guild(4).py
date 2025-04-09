n = int(input())
arr = list(map(int, input().split()))
arr.sort()

count = 0
team = 0
for i in arr:
    count += 1
    if i <= count:
        team += 1
        count = 0

print(team)