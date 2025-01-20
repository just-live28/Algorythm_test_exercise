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

v, e = map(int, input().split())

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

q = []
for _ in range(e):
    a, b, c = map(int, input().split())
    heapq.heappush(q, (c, a, b))

result = 0
while q:
    cost, a, b = heapq.heappop(q)
    
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)