n, m = map(int, input().split())

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
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

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, len(line) + 1):
        if line[j-1] == 1:
            union_parent(parent, i , j)

plans = list(map(int, input().split()))

is_possible = True
prev = plans[0]
for plan in plans[1:]:
    if find_parent(parent, prev) != find_parent(parent, plan):
        is_possible = False
        break
    else:
        prev = plan

print('YES') if is_possible == True else print('NO')