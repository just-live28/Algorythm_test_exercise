# 경로 압축(필수적으로 하자)
def find_parent(x):
    if parent[x] > 0:
        parent[x] = find_parent(parent[x])
    return parent[x]

parent = [-1] * 1000

# union-by-rank 최적화(선택사항. 위의 경로압축을 해도 시간초과가 날 경우)
def optimized_union_parent(u, v):
    u = find_parent(u)
    v = find_parent(v)
    
    if u == v:
        return False
    
    if parent[u] > parent[v]:
        u, v = v, u
    if parent[u] == parent[v]:
        parent[u] -= 1
    parent[v] = u
    return True

# 기본 union
def union_parent(u, v):
    u = find_parent(u)
    v = find_parent(v)
    
    if u == v:
        return False
    
    if u > v:
        parent[u] = v
    else:
        parent[v] = u
    return True