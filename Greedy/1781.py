import heapq
import sys
input = sys.stdin.readline

n = int(input())
problems = []
for _ in range(n):
    a, b = map(int, input().split())
    problems.append((a, b))
problems.sort(key = lambda x : (x[0], -x[1]))

time = 0
result = []
for dead_line, ramen in problems:
    if time < dead_line:
        time += 1
        heapq.heappush(result, ramen)
    elif ramen > result[0]:
        heapq.heappop(result)
        heapq.heappush(result, ramen)

print(sum(result))