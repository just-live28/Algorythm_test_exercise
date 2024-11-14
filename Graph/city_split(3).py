import heapq
import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

q = []
for _ in range(m):
    a, b, c = map(int, input().split())

    heapq.heappush(q, (c, a, b))

total = 0
max_cost = 0
while q:
    cost, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total += cost

        if cost > max_cost:
            max_cost = cost

print(total - max_cost)
