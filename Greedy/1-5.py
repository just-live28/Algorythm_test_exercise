from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0
for pair in combinations(balls, 2):
    ball1, ball2 = pair[0], pair[1]
    if ball1 == ball2:
        continue
    result += 1

print(result)