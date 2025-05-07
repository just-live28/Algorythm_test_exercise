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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

result = 0
is_cycle = False
for t in range(1, m+1):
    a, b = map(int, input().split())
    
    if is_cycle:
        continue
    
    if find_parent(a) == find_parent(b):
        result = t
        is_cycle = True
    else:
        union_parent(a, b)

print(result)