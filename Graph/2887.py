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
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

edge_x = []
edge_y = []
edge_z = []
for i in range(1, n+1):
    a, b, c = map(int, input().split())
    edge_x.append((a, i))
    edge_y.append((b, i))
    edge_z.append((c, i))
edge_x.sort()
edge_y.sort()
edge_z.sort()

q = []
for i in range(1, n):
    heapq.heappush(q, (edge_x[i][0] - edge_x[i-1][0], edge_x[i][1], edge_x[i-1][1]))
    heapq.heappush(q, (edge_y[i][0] - edge_y[i-1][0], edge_y[i][1], edge_y[i-1][1]))
    heapq.heappush(q, (edge_z[i][0] - edge_z[i-1][0], edge_z[i][1], edge_z[i-1][1]))

connect = 0
result = 0
while q:
    if connect == n-1:
        break
    
    dist, a, b = heapq.heappop(q)

    if find_parent(a) != find_parent(b):
        connect += 1
        result += dist
        union_parent(a, b)

print(result)