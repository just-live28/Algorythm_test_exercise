# n 보석 개수 k 가방 개수

# 보석, 가방을 무게 순으로 정렬
# 가방을 처음 것부터 뒤지기 시작. max_value_q 생성(heapq)
# 가방의 무게를 기준으로 담을 수 없는 보석이 나올 때까지(+idx가 n이 될 때까지) max_value_q에 보석을 추가, idx += 1
# max_value_q에서 heappop한 보석을 해당 가방에 넣는다. (총 가격 합계에 합산)
# 다음 가방으로 넘어가서 동일하게 반복(이 때 max_value_q의 보석들은 남아있는 상태)

import heapq
import sys
input = sys.stdin.readline

jewels = []
n, k = map(int, input().split())
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m, v))
bags = []
for _ in range(k):
    bags.append(int(input()))
jewels.sort()
bags.sort()

result = 0
max_q = []
jewel_idx = 0
for bag in bags:
    while jewel_idx < n and jewels[jewel_idx][0] <= bag:
        heapq.heappush(max_q, -jewels[jewel_idx][1])
        jewel_idx += 1
    
    if max_q:
        result += -heapq.heappop(max_q)
    
print(result)