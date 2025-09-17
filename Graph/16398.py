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

edges = []
for i in range(1, n+1):
    line = list(map(int, input().split()))
    
    for j in range(1, n+1):
        if i == j:
            continue
        
        edges.append((line[j-1], i, j))

edges.sort()

result = 0
connected = 0
for cost, planet1, planet2 in edges:
    if connected == n-1:
        break
    
    if find_parent(planet1) != find_parent(planet2):
        result += cost
        connected += 1
        union_parent(planet1, planet2)

print(result)