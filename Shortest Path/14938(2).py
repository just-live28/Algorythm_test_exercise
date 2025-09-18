# 플로이드로 모든 정점 쌍의 최소 거리를 계산
# 수색범위 내 도달 가능한 정점의 아이템 개수를 합산 -> 최대 구하기
# n 지역 / m 수색범위 / r 길 개수(양방향)
INF = int(1e9)

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(r):
    a, b, l = map(int, input().split())
    
    distance[a][b] = l
    distance[b][a] = l

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

max_result = 0
for i in range(1, n+1):
    count = items[i]
    
    for j in range(1, n+1):
        if i == j:
            continue
        
        if distance[i][j] <= m:
            count += items[j]
    
    max_result = max(max_result, count)

print(max_result)