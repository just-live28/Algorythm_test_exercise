# N개의 집, M개의 길(양방향)
# 2개의 분리된 마을로 분할
# 마을은 집들이 서로 연결되도록 분할해야 함

# 1. 크루스칼을 통해 마을을 서로 연결하면서 최소 유지비용을 구한다.
# 2. 돈이 가장 많이 드는 길로 연결된 집을 분할해버린다. -> 마을이 두개가 된다.
import heapq

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

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

q = []
for _ in range(m):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

total_cost = 0
max_cost = 0
while q:
    cost, a, b = heapq.heappop(q)
    
    if find_parent(parent, a) != find_parent(parent, b):
        total_cost += cost
        max_cost = cost
        union_parent(parent, a, b)

print(total_cost - max_cost)