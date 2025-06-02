import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    s, t = map(int, input().split())
    arr.append((s, t))
arr.sort(key = lambda x : (x[0], x[1]))

result = 1
q = []
heapq.heappush(q, 0)
for st, en in arr:
    if st >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, en)
    else:
        result += 1
        heapq.heappush(q, en)

print(result)