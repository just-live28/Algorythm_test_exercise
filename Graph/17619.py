import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a == b:
        return
    
    if ends[a] < ends[b]:
        a, b = b, a
    parent[b] = a
    ends[a] = max(ends[a], ends[b])

n, q = map(int, input().split())
logs = []
for i in range(1, n+1):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, i))
logs.sort()

parent = [i for i in range(n+1)]
ends = [0] * (n+1)
for _, x2, i in logs:
    ends[i] = x2

prev_x1, prev_x2, prev_idx = logs[0]
for i in range(1, n):
    x1, x2, idx = logs[i]
    if prev_x2 >= x1:
        union_parent(prev_idx, idx)
        prev_x2 = max(prev_x2, x2)
    else:
        prev_x1, prev_x2, prev_idx = x1, x2, idx

for _ in range(q):
    l1, l2 = map(int, input().split())
    
    if find_parent(l1) == find_parent(l2):
        print(1)
    else:
        print(0)