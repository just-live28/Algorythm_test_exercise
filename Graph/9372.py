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

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b = map(int, input().split())
        edges.append((a, b))

    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i

    result = 0
    for a, b in edges:
        if find_parent(a) != find_parent(b):
            result += 1
            union_parent(a, b)

    print(result)