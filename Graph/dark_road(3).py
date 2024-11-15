import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

q = []

entire_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    heapq.heappush(q, (z, x, y))
    entire_cost += z

min_cost = 0
while q:
    cost, x, y = heapq.heappop(q)

    if find_parent(parent, x) != find_parent(parent, y):
        min_cost += cost
        union_parent(parent, x, y)

print(entire_cost - min_cost)