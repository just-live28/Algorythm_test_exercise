INF = int(1e9)  # 무한을 의미하는 값 10억 설정

# 노드 개수 및 간선 개수 입력
v = int(input())
e = int(input())
# 2차원 최단 거리 테이블 선언, 모든 값을 무한으로 초기화
distance = [[INF] * (v+1) for _ in range(v+1)]
# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for i in range(1, v+1):
    for j in range(1, v+1):
        if i == j:
            distance[i][j] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    distance[a][b] = c
    
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

# 수행된 결과 출력
for i in range(1, v+1):
    for j in range(1, v+1):
        # 도달할 수 없는 경우, 무한(INFINITY)을 출력
        if distance[i][j] == INF:
            print("INFINITY", end=' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(distance[i][j], end=' ')
    print()