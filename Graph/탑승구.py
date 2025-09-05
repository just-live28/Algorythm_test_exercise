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

g = int(input())
p = int(input())
parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i
    
count = 0
for _ in range(p):
    dock_num = int(input())
    
    if parent[dock_num] == 0:
        break
    
    union_parent(dock_num, dock_num-1)
    count += 1

print(count)