import heapq

n = int(input())

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

parent = [0] * n
for i in range(n):
    parent[i] = i

x_list = []
y_list = []
z_list = []
for i in range(n):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))

x_list.sort()
y_list.sort()
z_list.sort()

q = []
for i in range(n-1):
    heapq.heappush(q, (x_list[i+1][0] - x_list[i][0], x_list[i][1], x_list[i+1][1]))
    heapq.heappush(q, (y_list[i+1][0] - y_list[i][0], y_list[i][1], y_list[i+1][1]))
    heapq.heappush(q, (z_list[i+1][0] - z_list[i][0], z_list[i][1], z_list[i+1][1]))

result = 0
while q:
    cost, a, b = heapq.heappop(q)
    
    if find_parent(parent, a) != find_parent(parent, b):
        result += cost
        union_parent(parent, a, b)

print(result)