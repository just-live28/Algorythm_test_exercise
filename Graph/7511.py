import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a == b:
        return False
    if parent[a] > parent[b]:
        a, b = b, a
    if parent[a] == parent[b]:
        parent[a] -= 1
    parent[b] = a
    return True

tc = int(input())
for i in range(tc):
    n = int(input())
    m = int(input())
    parent = [-1] * (n+1)
    for _ in range(m):
        u, v = map(int, input().split())
        union_parent(parent, u, v)
    l = int(input())
    result = []
    for _ in range(l):
        u, v = map(int, input().split())
        if find_parent(parent, u) == find_parent(parent, v):
            result.append(1)
        else:
            result.append(0)
    print(f"Scenario {i+1}:")
    for r in result:
        print(r)
    print()