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

n = int(input())
m = int(input())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    line = list(map(int, input().split()))
    for j in range(1, n+1):
        if i == j:
            continue
        
        if line[j-1] == 1 and find_parent(i) != find_parent(j):
            union_parent(i, j)

plans = list(map(int, input().split()))
parent_city = find_parent(plans[0])
enable = True
for i in range(1, m):
    if parent_city != find_parent(plans[i]):
        enable = False
        break

if enable:
    print('YES')
else:
    print('NO')