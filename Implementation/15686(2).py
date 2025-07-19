from itertools import combinations

n, m = map(int, input().split())
chickens = []
houses = []
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j-1] == 1:
            houses.append((i, j))
        elif line[j-1] == 2:
            chickens.append((i, j))

min_length = int(1e9)
for each_chickens in combinations(chickens, m):
    length = 0
    for hx, hy in houses:
        each_length = int(1e9)
        for cx, cy in each_chickens:
            each_length = min(each_length, abs(hx-cx) + abs(hy-cy))
        length += each_length
    
    min_length = min(min_length, length)
    
print(min_length)