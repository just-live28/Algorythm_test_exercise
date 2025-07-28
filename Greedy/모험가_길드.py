n = int(input())
arr = list(map(int, input().split()))
arr.sort()

team = 0
cur = 0
for i in arr:
    if cur + 1 >= i:
        team += 1
        cur = 0
    else:
        cur += 1

print(team)