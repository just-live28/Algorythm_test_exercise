import heapq
INF = int(1e9)  # 무한을 의미하는 값 10억 설정

# 노드 개수, 간선 개수 입력
v, e = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())
# 각 노드의 인접 노드 정보를 담는 리스트
graph = [[] for _ in range(v+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (v+1)

# 모든 간선 정보 입력
for _ in range(e):
    # a 노드에서 b 노드로 가는 데 비용 c가 든다는 의미
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로 0으로 설정 및 큐 삽입
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:    # 큐가 빌 때까지
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if dist > distance[now]:
            continue
        # 현재 노드와 연결된 다른 인접 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)
# 시작 노드에서 다른 모든 노드로 가는 최단 거리를 출력
for i in range(1, v + 1):
	# 도달할 수 없는 경우, 무한(INFINITY)을 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])