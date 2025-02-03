import sys
sys.setrecursionlimit(10000)
input = lambda: sys.stdin.readline().rstrip()

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

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

result = 0
connected = 0
for cost, node1, node2 in edges:
    if connected == v-1:
        break
    
    if find_parent(parent, node1) != find_parent(parent, node2):
        result += cost
        connected += 1
        union_parent(parent, node1, node2)

print(result)