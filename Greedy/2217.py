# 특정 로프를 병렬로 연결한 뒤, 가장 작은 로프의 최대 중량이 답이다.

# 큰 로프 순으로 정렬한 뒤,
# 로프를 하나씩 늘려가면서 가장 뒤 로프가 견딜 수 있는 최대 중량이 총 최대 중량을 넘어서면 갱신한다.

n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)

max_weight = 0
for i in range(n):
    max_weight = max(max_weight, ropes[i] * (i+1))

print(max_weight)