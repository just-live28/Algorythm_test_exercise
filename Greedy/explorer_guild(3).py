n = int(input())
array = list(map(int, input().split()))
array.sort()

current = 0
team = 0
for i in array:
    if current + 1 >= i:
       current = 0
       team += 1
    else:
        current += 1

print(team) 