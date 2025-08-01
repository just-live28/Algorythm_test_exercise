# N개의 여행지(1~N번) / 양방향 / 인접 행렬
# 행렬마다, 1인 여행지와 서로소 집합 연결(union)
# 이후 여행계획 두개씩 잡고, 서로 같은 집합인지 판단(하나라도 다른 집합이라면 No, 아니면 Yes)

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

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for i in range(1, n+1):
    line = list(map(int, input().split()))

    for j in range(1, n+1):
        if line[j-1] == 1:
            union_parent(i, j)

plans = list(map(int, input().split()))
prev = plans[0]
enable = True
for i in range(1, m):
    if find_parent(prev) != find_parent(plans[i]):
        enable = False
        break
    else:
        prev = plans[i]
        
if enable:
    print('YES')
else:
    print('NO')