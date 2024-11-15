import sys
input = sys.stdin.readline

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



# g 탑승구 p 비행기
g = int(input())
p = int(input())

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

planes = []
for _ in range(p):
    planes.append(int(input()))

count = 0
for plane in planes:
    g = find_parent(parent, plane)

    if g == 0:
        break
    else:
        count += 1
        union_parent(parent, g, g-1)

print(count)