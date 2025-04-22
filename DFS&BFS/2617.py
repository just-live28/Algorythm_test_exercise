# 중간이려면? 홀수 개 기준 양쪽으로 같은 수 2 / 2
# 짝수 개 기준(왼쪽이 하나 더 많아야 함) 2 / 1

n, m = map(int, input().split())
graph_heavy = [[] for _ in range(n+1)]
graph_light = [[] for _ in range(n+1)]
mid = (n+1) // 2

for _ in range(m):
    a, b = map(int, input().split())
    graph_heavy[b].append(a)
    graph_light[a].append(b)

def dfs_heavy(visited, x):
    global count_heavy
    visited[x] = True
    
    for nxt in graph_heavy[x]:
        if not visited[nxt]:
            count_heavy += 1
            dfs_heavy(visited, nxt)
    
def dfs_light(visited, x):
    global count_light
    visited[x] = True
    
    for nxt in graph_light[x]:
        if not visited[nxt]:
            count_light += 1
            dfs_light(visited, nxt)

result = 0
for i in range(1, n+1):
    visited_heavy = [False] * (n+1)
    visited_light = [False] * (n+1)
    count_heavy, count_light = 0, 0
    
    dfs_heavy(visited_heavy, i)
    dfs_light(visited_light, i)
    
    if count_heavy >= mid or count_light >= mid:
        result += 1

print(result)