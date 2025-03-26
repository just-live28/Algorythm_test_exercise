import heapq
import sys
input = sys.stdin.readline

# max_heap 관련된 모든 "수"는 음수 처리해야 한다.
max_heap = []
min_heap = []
n = int(input())
for _ in range(n):
    num = int(input())
    
    if not max_heap:
        heapq.heappush(max_heap, -num)
        print(-max_heap[0])
        continue
    
    if num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if len(max_heap) < len(min_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    
    print(-max_heap[0])