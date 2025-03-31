# find: 특정 원소가 속한 집합 찾기
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# union: 두 원소가 속한 집합 합치기
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드 개수와 간선(union 연산)의 개수 입력
v, e = map(int, input().split())
parent = [0] * (v+1)    # 부모 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
total_min_cost = 0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    # 비용 순으로 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((c, a, b))

# 간선을 비용 순으로 정렬
edges.sort()

count = 0   # 연결된 간선 갯수
# 간선을 하나씩 확인
for cost, a, b in edges:
    # 간선이 v-1 개 연결된 경우 종료
    if count == v-1:
        break
    
    # 사이클이 발생하지 않는 경우 집합에 포함.
    # 연결된 간선 갯수를 1 올리고, 최종 비용에 해당 비용을 추가
    if find_parent(a) != find_parent(b):
        count += 1
        total_min_cost += cost
        union_parent(a, b)

print(total_min_cost)