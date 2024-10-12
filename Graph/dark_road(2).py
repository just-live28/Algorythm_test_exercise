n, m = map(int, input().split())

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

parent = [0] * n

for i in range(n):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    
    edges.append((c, a, b))

edges.sort()

total_cost = 0
discounted_cost = 0
for edge in edges:
    cost, a, b = edge
    
    total_cost += cost
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        discounted_cost += cost

print(total_cost - discounted_cost)