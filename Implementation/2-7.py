from itertools import combinations

n, m = map(int, input().split())

houses = []
chickens = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] == 1:
            houses.append((a, b))
        elif line[b-1] == 2:
            chickens.append((a, b))

def cal_total_length(chickens, houses):
    total_length = 0
    for hx, hy in houses:
        min_length = int(1e9)
        for cx, cy in chickens:
            min_length = min(min_length, abs(hx - cx) + abs(hy - cy))
        total_length += min_length

    return total_length

min_total_length = int(1e9)
for each_chickens in combinations(chickens, m):
    each_total_length = cal_total_length(each_chickens, houses)
    min_total_length = min(min_total_length, each_total_length)

print(min_total_length)