import sys
input = sys.stdin.readline

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

n = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

x_edge = []
y_edge = []
z_edge = []
edges = []

for i in range(1, n+1):
    x, y, z= map(int, input().split())
    x_edge.append((x, i))
    y_edge.append((y, i))
    z_edge.append((z, i))

x_edge.sort()
y_edge.sort()
z_edge.sort()

# x_edge[i] / x_edge[i+1] / [0] 좌표 [1] 행성번호
for i in range(n-1):
    edges.append((abs(x_edge[i][0] - x_edge[i+1][0]), x_edge[i][1], x_edge[i+1][1]))
    edges.append((abs(y_edge[i][0] - y_edge[i+1][0]), y_edge[i][1], y_edge[i+1][1]))
    edges.append((abs(z_edge[i][0] - z_edge[i+1][0]), z_edge[i][1], z_edge[i+1][1]))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)