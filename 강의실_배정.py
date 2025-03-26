import heapq
import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))
classes.sort()

q = []
heapq.heappush(q, 0)
for s, t in classes: 
    if s >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, t)

print(len(q))