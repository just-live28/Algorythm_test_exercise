#  n * n 의 도시

# city[r][c] = 0, 1, 2 
# r,c는 1부터 시작
# 0은 빈칸 1은 집 2는 치킨집

# 집과 치킨집 거리 : abs(x1 - x2) + abs(y1 - y2)
# 치킨집을 폐업하려고 함. M개를 고르고 나머지를 폐업.


# 집과 빈칸만이 있는 board
#치킨집 배열에서 M개를 골라 new_board에 넣기

# 순서 x 중복 x -> 조합(combinations)

import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

houses = []
stores = []
for a in range(1, n+1):
    line = list(map(int, input().split()))
    for b in range(1, n+1):
        if line[b-1] == 1:
            houses.append((a, b))
        elif line[b-1] == 2:
            stores.append((a, b))

min_chicken_length = int(1e9)
for shops in list(combinations(stores, m)):
    total = 0
    for house in houses:
        min_length = int(1e9)
        
        for shop in shops:
            length = abs(house[0] - shop[0]) + abs(house[1] - shop[1])
            if length < min_length:
                min_length = length
        
        total += min_length
    
    if total < min_chicken_length:
        min_chicken_length = total

print(min_chicken_length)