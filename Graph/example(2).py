#서로소 집합 알고리즘 (find, union)
# find_parent(parent, x) : x 노드의 부모 노드를 반환
# union_parent(parent, a, b) : a, b 노드의 각 부모 노드를 구해 부모 노드가 더 작은 노드로 연결

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

v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

print("부모 테이블 : ", end=' ')
for i in range(1, v+1):
    print(parent[i], end=' ')
print()
print("각 원소가 속한 집합 : ", end=' ')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
