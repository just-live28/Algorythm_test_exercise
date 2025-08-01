n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

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

    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if line[j-1] == 1:
            union_parent(parent, i, j)

plans = list(map(int, input().split()))

prev = plans[0]
is_enable = True
for i in range(1, m):
    if find_parent(parent, prev) != find_parent(parent, plans[i]):
        is_enable = False
        break
    else:
        prev = plans[i]

if is_enable:
    print('YES')
else:
    print('NO')