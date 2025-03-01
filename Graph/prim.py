import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

tree = [False] * (v+1)
tree[1] = True
q = []
for b, cost in graph[1]:
    heapq.heappush(q, (cost, b))

count = 0
result = 0
while count < v-1:
    cost, now = heapq.heappop(q)
    
    if tree[now]:
        continue
    
    tree[now] = True
    count += 1
    result += cost
    for b, cost in graph[now]:
        if not tree[b]:
            heapq.heappush(q, (cost, b))

print(result)