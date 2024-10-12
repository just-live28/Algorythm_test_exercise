# 최소 비용으로 모든 집을 연결 -> 크루스칼
# 2개의 마을로 나누어야 하므로, 크루스칼로 연결한 다음 비용이 가장 큰 도로와 연결된 집을 분리
# 결론적으로 크루스칼 알고리즘 후 나온 total cost에서 가장 비용이 큰 cost를 제거

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    
    edges.append((c, a, b))

edges.sort()

result = []
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent ,b):
        result.append(cost)
        union_parent(parent, a, b)

result.pop()
print(sum(result))