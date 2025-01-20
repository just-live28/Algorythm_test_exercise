# 0 ~ N번 번호
# 0 a b / 1 a b
# 0 합친다 / 1 같은팀인지 확인

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

N, M = map(int, input().split())

parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i

for _ in range(M):
    oper, a, b = map(int, input().split())
    
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")