import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(u, v):
    u = find_parent(u)
    v = find_parent(v)
    
    if u == v:
        return False
    if parent[u] > parent[v]:
        u, v = v, u
    if parent[u] == parent[v]:
        parent[u] -= 1
    parent[v] = u
    return True

v, e = map(int, input().split())
parent = [-1] * (v+1)
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
count = 0
for cost, a, b in edges:
    if count == v-1:
        break
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        count += 1

print(result)