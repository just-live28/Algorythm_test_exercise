from collections import deque

# 테스트 케이스 다 맞은 나의 불쌍한 코드..
n = int(input())
index = [0] * (n+1)
for i in range(1, n+1):
    index[i] = i

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]
unorder = []
for i in range(1, n+1):
    line = input()
    for j in range(1, n+1):
        if line[j-1] == '1':
            graph[i].append(j)
            reverse_graph[j].append(i)
            if i > j:
                unorder.append((i, j))
                
def try_enqueue(a, b):
    if ((a, b) in visited and visited[(a, b)] > 3) or ((b, a) in visited and visited[(b, a)] > 3):
        return
    elif (a, b) in visited:
        visited[(a, b)] += 1
    else:
        visited[(a, b)] = 1
    q.append((a, b))
    
def check_all_edges(graph):
    for i in range(1, n+1):
        for j in graph[i]:
            if index[i] > index[j]:
                return False
    return True

def topology_sort(graph):
    indegree = [0] * (n+1)
    for i in range(1, n+1):
        for j in graph[i]:
            indegree[j] += 1
    
    topology_q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            topology_q.append(i)
    
    result = []
    while topology_q:
        now = topology_q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                topology_q.append(i)
    
    return result

visited = {}
q = deque(unorder)
while q:
    u, v = q.popleft()
    index[u], index[v] = index[v], index[u]
    
    for i in graph[u]:
        if index[u] > index[i]:
            try_enqueue(u, i)
    for i in graph[v]:
        if index[v] > index[i]:
            try_enqueue(v, i)
    for i in reverse_graph[u]:
        if index[u] < index[i]:
            try_enqueue(i, u)
    for i in reverse_graph[v]:
        if index[v] < index[i]:
            try_enqueue(i, v)

# graph 전체 간선이 조건을 만족하는지 검사 : 통과 시 위상 정렬 진행, 
if not check_all_edges(graph):
    print(-1)
else:
    result = topology_sort(graph)
    a = [0] * (n+1)
    for i in range(1, n+1):
        a[result[i-1]] = i
    print(*a[1:])