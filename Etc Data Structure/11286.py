# 절댓값 최소 힙
# (abs값, 실제값)

import heapq
import sys
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if q:
            print(heapq.heappop(q)[1])
        else:
            print(0)
    else:
        heapq.heappush(q, (abs(num), num))