import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

def topological_sort():
    q = []
    for i in range(1, n+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    
    result = []
    while q:
        now = heapq.heappop(q)
        result.append(now)
        
        for nxt in graph[now]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(q, nxt)
    
    return result

print(*topological_sort())