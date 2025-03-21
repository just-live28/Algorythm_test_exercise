import heapq
import sys
input = sys.stdin.readline

max_q = []
min_q = []
n = int(input())
for _ in range(n):
    num = int(input())
    
    if not max_q:
        heapq.heappush(max_q, -num)
    else:
        if num > -max_q[0]:
            heapq.heappush(min_q, num)
        else:
            heapq.heappush(max_q, -num)
    
    if len(max_q) < len(min_q):
        heapq.heappush(max_q, -heapq.heappop(min_q))
    elif len(max_q) - len(min_q) > 1:
        heapq.heappush(min_q, -heapq.heappop(max_q))
    
    print(-max_q[0])