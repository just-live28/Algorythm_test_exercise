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

# 탑승구 수
g = int(input())

parent = [0] * (g+1)

for i in range(1, g+1):
    parent[i] = i

p = int(input())
airplanes = []
for _ in range(p):
    airplanes.append(int(input()))

result = 0
is_full = False
for i in airplanes:
    root = find_parent(parent, i)
    if root != 1:
        union_parent(parent, root, root-1)
        result += 1
    else:
        if is_full == True:
            break
        else:
            is_full = True
            result += 1

print(result)
        
