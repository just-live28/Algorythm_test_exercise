# 1~N 번의 강의
# 각 줄) 시간 선수과목.. -1

# 1을 들어야 2를 들을수 있다면 
# graph[1].append(2) / indegree[2] += 1

from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1)
times = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    
    times[i] = line[0]
    
    for course in line[1:-1]:
        indegree[i] += 1
        graph[course].append(i)

def topology_sort():
    result = copy.deepcopy(times)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        # now가 하위 과목
        now = q.popleft()
        # i가 상위 과목
        for i in graph[now]:
            indegree[i] -= 1
            
            result[i] = max(result[i], times[i] + result[now])
            
            if indegree[i] == 0:
                q.append(i)
        
    for i in range(1, n+1):
        print(result[i])

topology_sort()