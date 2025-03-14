# 외판원 순회
# N개의 도시(1sided), 도시 사이 길이 있을수도 있고 없을 수도 있음
# 한 도시에서 출발해 N개의 도시를 "모두" 거쳐 다시 원래의 도시로 돌아오는 경로
# 단, 한 번 갔던 도시로는 다시 갈 수 없다. (한붓그리기)
# 가장 적은 비용으로 순회하기

# 첫 도시 방문 처리 안 함
# 모든 도시가 방문처리 되었을 경우의 최소 비용
# 백트래킹
# func(k, total_cost) : k개의 도시를 방문한 상태. index k번째 도시를 선택하는 함수

n = int(input())
graph = [[] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        graph[i].append(line[j])

visited = [False] * n
def func(k, init, cur, total_cost):
    global min_total_cost
    if k == n:
        if graph[cur][init] != 0:
            min_total_cost = min(min_total_cost, total_cost + graph[cur][init])
        return
    
    for next in range(n):
        if not visited[next] and graph[cur][next] != 0:
            visited[next] = True
            func(k+1, init, next, total_cost + graph[cur][next])
            visited[next] = False

min_total_cost = 1000000 * n + 1
for init in range(n):
    visited[init] = True
    func(1, init, init, 0)
    visited[init] = False

print(min_total_cost)