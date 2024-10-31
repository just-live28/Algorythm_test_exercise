# n 맵 크기 / m 영업 가능 치킨집 수
# 0 빈칸 1 집 2 치킨집

#치킨집은 따로 분리
#0과 1만 세팅된 board를 가져다가 치킨집 세팅 후 함수 진행
from itertools import combinations

n, m = map(int, input().split())

stores = []
houses = []

for a in range(n):
    line = list(map(int, input().split()))
    for b in range(n):
        if line[b] == 1:
            houses.append((a,b))
        if line[b] == 2:
            stores.append((a,b))

min_length = int(1e9)
for chickens in combinations(stores, m):
    total_length = 0
    for hx, hy in houses:
        each_length = int(1e9)
        for cx, cy in chickens:
            distance = abs(hx-cx) + abs(hy-cy)
            if distance < each_length:
                each_length = distance
        total_length += each_length
    
    if total_length < min_length:
        min_length = total_length

print(min_length)