import heapq

def topology_sort():
  result = [0] * (n+1)
  
  q = []
  for i in range(1, n+1):
    if indegree[i] == 0:
      heapq.heappush(q, i)
  
  N = 1
  while q:
    now = heapq.heappop(q)
    result[now] = N
    N += 1
    
    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        heapq.heappush(q, i)
  
  return result

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
  line = input()
  for j in range(1, n+1):
    if i == j:
      continue
    if line[j-1] == '1':
      indegree[j] += 1
      graph[i].append(j)

result = topology_sort()

if result.count(0) > 1:
  print(-1)
else:
  print(*result[1:])