n = int(input())
arr = list(map(int, input().split()))
arr.sort()

team = 0
current = 0
for i in arr:
    current += 1
    if current >= i:
        team += 1
        current = 0

print(team)