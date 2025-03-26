import heapq
import sys
input = sys.stdin.readline

n = int(input())
lines = []
for _ in range(n):
    h, o = map(int, input().split())
    if h > o:
        h, o = o, h
    lines.append((h, o))
lines.sort(key = lambda x : (x[1]))
d = int(input())

result = 0
enable_lines = []
for h, o in lines:
    heapq.heappush(enable_lines, h)
    
    d_st = o - d
    while enable_lines and enable_lines[0] < d_st:
        heapq.heappop(enable_lines)
    result = max(result, len(enable_lines))

print(result)