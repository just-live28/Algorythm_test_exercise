n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if i == j:
            continue
        if line[j-1] == 1:
            union_parent(parent, i, j)

trips = list(map(int, input().split()))
enable = True
prev = trips[0]
for i in range(1, m):
    if find_parent(parent, prev) != find_parent(parent, trips[i]):
        enable = False
        break
    else:
        prev = trips[i]

if enable:
    print("YES")
else:
    print("NO")