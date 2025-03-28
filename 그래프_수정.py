import heapq
import sys

input = sys.stdin.readline

def topology_sort():
  q = []
  for i in range(1, n+1):
    if indegree[i] == 0:
      heapq.heappush(q,-i)
  
  N = n
  while q:
    now = -heapq.heappop(q)
    answer[now] = N
    
    for i in node[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(q, -i)
    N -= 1

n = int(input())
node = [[] for _ in range((n+1))]
indegree = [0] * (n+1)

for v in range(1, n+1):
  temp = [0]+ list(map(int, input().strip()))
  for i in range(1, n+1):
    if temp[i] == 1:
      node[i].append(v)
      indegree[v] += 1

answer = [0]*(n+1)

topology_sort()
if answer.count(0) > 1:
  print(-1)
else:
  print(*answer[1:])