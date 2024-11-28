import heapq
import sys
input = sys.stdin.readline

q = []
n = int(input())

for _ in range(n):
    num = int(input())
    
    if num == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
        continue
    
    heapq.heappush(q, num)