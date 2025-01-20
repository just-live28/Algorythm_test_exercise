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

parent = [0] * n
for i in range(1, n):
    parent[i] = i

q = []
for _ in range(m):
    x, y, z = map(int, input().split())
    
    heapq.heappush(q, (z, x, y))

total = 0
min_total = 0
while q:
    cost, x, y = heapq.heappop(q)
    
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        min_total += cost
    total += cost

print(total - min_total)