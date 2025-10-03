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
        components[a] += components[b]
    else:
        parent[a] = b
        components[b] += components[a]

n = int(input())
parent = [0] * 1000001
for i in range(1, 1000001):
    parent[i] = i
components = [1] * 1000001

for _ in range(n):
    oper = input().rstrip().split()
    
    if oper[0] == 'I':
        c1 = int(oper[1])
        c2 = int(oper[2])
        
        if find_parent(c1) != find_parent(c2):
            union_parent(c1, c2)
    elif oper[0] == 'Q':
        target = find_parent(int(oper[1]))
        print(components[target])