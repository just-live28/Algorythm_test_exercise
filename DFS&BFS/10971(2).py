#TSP
# 도시 N개(1~N), 도시 사이 길이 있음(없을 수도 있음)
# 한 도시에서 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 복귀
# 한 번 갔던 도시로는 다시 갈 수 없다(마지막 출발지로 복귀하는 것 제외)
# 가장 적은 비용으로 이를 수행

# 인접 행렬 방식 데이터. (단방향). 자기 자신은 항상 0, 길이 없는 경우 0

# 백트래킹
# func(k, init, cur, cur_cost) : k 개의 도시를 방문한 상태. idx k번째 도시를 방문하는 함수
# k == n 인 경우 cur->init 길이 있으면 cur_cost에 더하고 cur_cost와 min_cost를 비교 후 return
# 일반적으로, visited를 돌며 미방문 & 비용이 0이 아닌 도시에 대해 방문 처리 후 func(k+1, init, next, cur_cost + graph[cur][next]) 호출
# 그 뒤 다시 방문 처리한 도시 미방문 처리
# 함수 작성 후, 모든 도시를 돌며 방문 처리 후 최초 실행 func(1, start, start, 0), 이후 미방문 처리

n = int(input())
graph = [[0] for _ in range(n+1)]
for i in range(1, n+1):
    graph[i].extend(list(map(int, input().split())))

def func(k, init, cur, cur_cost):
    global min_cost
    if k == n:
        if graph[cur][init] != 0:
            min_cost = min(min_cost, cur_cost + graph[cur][init])
        return
    
    for next in range(1, n+1):
        if not visited[next] and graph[cur][next] != 0:
            visited[next] = True
            func(k+1, init, next, cur_cost + graph[cur][next])
            visited[next] = False

min_cost = 1000000 * n + 1
visited = [False] * (n+1)
for start in range(1, n+1):
    visited[start] = True
    func(1, start, start, 0)
    visited[start] = False

print(min_cost)