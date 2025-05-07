import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

total_cost = 0
connect_count = 0
recent_cost = 0
for cost, a, b in edges:
    if connect_count == n-1:
        break
    
    if find_parent(a) != find_parent(b):
        connect_count += 1
        total_cost += cost
        union_parent(a, b)
        recent_cost = cost

print(total_cost - recent_cost)