# I 삽입 D 삭제
# D 삭제 : 1 최댓값 / -1 최솟값 (비어있는 경우 연산 무시)

import heapq
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    min_q = []
    max_q = []
    deleted = {}
    k = int(input())
    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            deleted[num] = deleted.get(num, 0) + 1
        else:
            if not deleted:
                continue
                    
            if num == 1:
                while max_q:
                    max_num = -heapq.heappop(max_q)
                    if deleted.get(max_num, 0) > 0:
                        deleted[max_num] -= 1
                        if deleted[max_num] == 0:
                            del deleted[max_num]
                        break
            else:
                while min_q:
                    min_num = heapq.heappop(min_q)
                    if deleted.get(min_num, 0) > 0:
                        deleted[min_num] -= 1
                        if deleted[min_num] == 0:
                            del deleted[min_num]
                        break
    
    while max_q and deleted.get(-max_q[0], 0) == 0:
        heapq.heappop(max_q)
    while min_q and deleted.get(min_q[0], 0) == 0:
        heapq.heappop(min_q)
    
    if not min_q or not max_q:
        print("EMPTY")
    else:
        print(-heapq.heappop(max_q), heapq.heappop(min_q))