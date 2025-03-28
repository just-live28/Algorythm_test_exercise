import sys
sys.setrecursionlimit(10000)

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
    
v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

result = 0
count = 0
for cost, a, b in edges:
    if count == v - 1:
        break
    
    if find_parent(a) != find_parent(b):
        count += 1
        result += cost
        union_parent(a, b)

print(result)