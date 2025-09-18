# 단방향 도로
# 왕복시간: distance[i][j] + distance[j][i]
# 갈 수 있는 도시만 선택 / 최대 왕복시간이 최소가 되는 도시
INF = int(1e9)

n, m = map(int, input().split())
distance = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(m):
    a, b, t = map(int, input().split())
    distance[a][b] = t
    
k = int(input())
homes = list(map(int, input().split()))
homes.sort()

for l in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][l] + distance[l][j])

min_total_length = INF
result = []

for i in range(1, n+1):
    max_length = 0
    for home in homes:
        if i == home:
            continue
        
        max_length = max(max_length, distance[home][i] + distance[i][home])
    
    if max_length < min_total_length:
        min_total_length = max_length
        result.clear()
        result.append(i)
    elif max_length == min_total_length:
        result.append(i)

print(*result)