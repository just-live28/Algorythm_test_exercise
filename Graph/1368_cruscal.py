import heapq

n = int(input()) + 1
parent = [-1] * (n+1)

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

q = []
for i in range(1, n):
    heapq.heappush(q, (int(input()), 0, i))
for i in range(1, n):
    line = list(map(int, input().split()))
    for j in range(1, n):
        if line[j-1] == 0:
            continue
        heapq.heappush(q, (line[j-1], i, j))

result = 0
count = 0
while q:
    if count == n-1:
        break
    
    cost, a, b = heapq.heappop(q)
    
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost
        count += 1

print(result)