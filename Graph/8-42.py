g = int(input())
p = int(input())

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

parent = [0] * (g+1)
for i in range(1, g+1):
    parent[i] = i

count = 0
enable_landing = True
for _ in range(p):
    target = int(input())
    
    if enable_landing == False:
        continue
    
    enable_gate = find_parent(parent, target)
    
    if enable_gate == 0:
        enable_landing = False
        continue
        
    union_parent(parent, target, enable_gate - 1)
    count += 1

print(count)