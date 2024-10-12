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

parent = [0] * (m+1)

for i in range(1, m+1):
    parent[i] = i

result = []
for _ in range(m):
    oper, a, b = map(int, input().split())
    
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent ,b):
            result.append("YES")
        else:
            result.append("NO")

for i in result:
    print(i)
