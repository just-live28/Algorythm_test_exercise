import heapq

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())

parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

x_planet = []
y_planet = []
z_planet = []

for i in range(1, n + 1):
    x, y, z = map(int, input().split())

    x_planet.append((x, i))
    y_planet.append((y, i))
    z_planet.append((z, i))

x_planet.sort()
y_planet.sort()
z_planet.sort()

q = []
for i in range(n - 1):
    heapq.heappush(q, (x_planet[i + 1][0] - x_planet[i][0], x_planet[i][1], x_planet[i + 1][1]))
    heapq.heappush(q, (y_planet[i + 1][0] - y_planet[i][0], y_planet[i][1], y_planet[i + 1][1]))
    heapq.heappush(q, (z_planet[i + 1][0] - z_planet[i][0], z_planet[i][1], z_planet[i + 1][1]))

total_cost = 0
while q:
    cost, a, b = heapq.heappop(q)

    if find_parent(parent, a) != find_parent(parent, b):
        total_cost += cost
        union_parent(parent, a, b)

print(total_cost)