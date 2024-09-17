import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())

graph = []
graph.append([])

for i in range(1, n+1):
    line = list(map(int, input().split()))
    line.insert(0, -1)
    graph.append(line)

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == 1:
            union_parent(parent, i, j)

plan = list(map(int, input().split()))

prev = plan[0]
is_possible = True
for i in range(1, m):
    if find_parent(parent, prev) != find_parent(parent, plan[i]):
        is_possible = False
        break
    prev = plan[i]

print('YES') if is_possible else print('NO')
    

