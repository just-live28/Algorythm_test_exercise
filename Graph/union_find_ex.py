# find : 특정 원소가 속한 집합 찾기
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# union : 두 원소가 속한 집합 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 개수 입력받기    
v, e = map(int, input().split())
parent = [0] * (v+1)    # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False   # 사이클 발생 여부

# 모든 간선에 대해 union 연산 수행
for _ in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(a) == find_parent(b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 합집합(union) 수행
    else:
        union_parent(a, b)

# 사이클이 발생한 경우 해당 문구 출력
if cycle:
    print("사이클이 발생했습니다.")
# 사이클이 발생하지 않은 경우 각 원소의 루트 노드 출력
else:
    print('각 원소의 루트 노드: ', end='')
    for i in range(1, v+1):
        print(find_parent(i), end=' ')