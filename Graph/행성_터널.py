import heapq
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

n = int(input())
x_loc = []
y_loc = []
z_loc = []
for i in range(1, n+1):
    x, y, z = map(int, input().split())
    x_loc.append((x, i))
    y_loc.append((y, i))
    z_loc.append((z, i))
x_loc.sort()
y_loc.sort()
z_loc.sort()

edges = []
for i in range(n-1):
    heapq.heappush(edges, (x_loc[i+1][0] - x_loc[i][0], x_loc[i][1], x_loc[i+1][1]))
    heapq.heappush(edges, (y_loc[i+1][0] - y_loc[i][0], y_loc[i][1], y_loc[i+1][1]))
    heapq.heappush(edges, (z_loc[i+1][0] - z_loc[i][0], z_loc[i][1], z_loc[i+1][1]))
    
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

connect = 0
result = 0
while edges:
    diff, idx1, idx2 = heapq.heappop(edges)
    
    if connect == n-1:
        break
    
    if find_parent(idx1) != find_parent(idx2):
        connect += 1
        result += diff
        union_parent(idx1, idx2)

print(result)