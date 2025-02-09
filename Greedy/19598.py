import sys
import heapq
input = sys.stdin.readline

n = int(input())
meetings = []
for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))
meetings.sort()

q = []
heapq.heappush(q, -1)

for i in range(n):
    start_time, end_time = meetings[i]
    if start_time >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, end_time)

print(len(q))