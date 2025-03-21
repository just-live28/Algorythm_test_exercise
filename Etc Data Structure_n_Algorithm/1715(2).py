# 작은거 두개를 묶어서 다시 넣기
# 하나를 꺼냈을 때 빌 때까지

import heapq
n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

count = 0
while True:
    card1 = heapq.heappop(q)
    if not q:
        break
    card2 = heapq.heappop(q)
    card_sum = card1 + card2
    count += card_sum
    heapq.heappush(q, card_sum)

print(count)