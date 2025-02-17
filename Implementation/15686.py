from itertools import combinations

n, m = map(int, input().split())
stores = []
houses = []
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            houses.append((i, j))
        elif line[j] == 2:
            stores.append((i, j))

min_total = int(1e9)
for alive_stores in combinations(stores, m):
    total = 0
    for hx, hy in houses:
        min_length = int(1e9)
        for sx, sy in alive_stores:
            length = abs(hx - sx) + abs(hy - sy)
            min_length = min(min_length, length)
        total += min_length
    min_total = min(min_total, total)

print(min_total)