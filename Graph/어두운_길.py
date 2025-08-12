# 절약 가능한 최대 금액

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
parent = [0] * n
for i in range(n):
    parent[i] = i
edges = []
total = 0
for _ in range(m):
    x, y, z = map(int, input().split())
    total += z
    edges.append((z, x, y))
edges.sort()

result = 0
count = 0
for cost, a, b in edges:
    if count == n-1:
        break
    
    if find_parent(a) != find_parent(b):
        result += cost
        count += 1
        union_parent(a, b)

print(total - result)