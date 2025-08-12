# n * n 도시
# 0 빈칸, 1 집, 2 치킨집
# 치킨 거리: 가장 가까운 치킨집과의 거리 abs(hx - cx) + abs(hy - cy)
# 최대 M개를 고른다. (순서 x, 중복x => 조합)
# 도시 치킨 거리(모든 집 치킨 거리 합)가 최소가 되도록
######
# 집과 치킨집 좌표 따로 기록
# 조합으로 치킨집에서 m개를 고르기
# 각 조합마다, 도시 치킨 거리를 구하기
from itertools import combinations

n, m = map(int, input().split())
homes = []
chickens = []
for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j-1] == 1:
            homes.append((i, j))
        elif line[j-1] == 2:
            chickens.append((i, j))

result = int(1e9)
for each_chickens in combinations(chickens, m):
    total_length = 0
    for hx, hy in homes:
        chicken_length = int(1e9)
        for cx, cy in each_chickens:
            chicken_length = min(chicken_length, abs(hx - cx) + abs(hy - cy))
        total_length += chicken_length
    result = min(result, total_length)

print(result)