# 작은 것들 두개 끼리를 합치기
# 합친 결과는 다시 힙큐에 넣기

import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

result = 0
while True:
    num1 = heapq.heappop(q)
    
    if not q:
        break
    
    num2 = heapq.heappop(q)
    
    result += num1 + num2
    heapq.heappush(q, num1 + num2)

print(result)