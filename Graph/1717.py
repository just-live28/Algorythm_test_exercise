import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [-1] * (n+1)

def find_parent(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, u, v):
    u = find_parent(parent, u)
    v = find_parent(parent, v)
    
    if u == v:
        return False
    if parent[u] > parent[v]:
        u, v = v, u
    if parent[u] == parent[v]:
        parent[u] -= 1
    parent[v] = u
    return True

for _ in range(m):
    oper, a, b = map(int, input().split())
    
    if oper == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")