# 간선이 축마다 존재한다.
# N개의 행성이 있다면, 3 * (N-1) 의 간선이 존재한다.

n = int(input())

def find_parent(parent, x):
    if parent[x] != x:
       parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent ,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

x_edges = []
y_edges = []
z_edges = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    
    x_edges.append((x, i))
    y_edges.append((y, i))
    z_edges.append((z, i))

x_edges.sort()
y_edges.sort()
z_edges.sort()

edges = []
for i in range(n-1):
    edges.append((abs(x_edges[i+1][0] - x_edges[i][0]), x_edges[i][1], x_edges[i+1][1]))
    edges.append((abs(y_edges[i+1][0] - y_edges[i][0]), y_edges[i][1], y_edges[i+1][1]))
    edges.append((abs(z_edges[i+1][0] - z_edges[i][0]), z_edges[i][1], z_edges[i+1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)