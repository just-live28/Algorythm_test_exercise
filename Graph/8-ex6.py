# 위상 정렬
# 1~N번(N개)의 강의 / 동시에 여러 강의 수강 가능
# 같은 위상을 가지고 있다면, 시간이 더 많이 걸리는 강의의 수강시간이 반영

# N번의 입력
# N번 강의의 수강시간, 선수과목들, -1
# N번째 줄 : t .... -1
from collections import deque

n = int(input())

indegree = [0] * (n+1)
times = [0] * (n+1)
d = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for i in range(1, n+1):
    line = list(map(int, input().split()))
    times[i] = line[0]
    d[i] = times[i]
    
    for j in line[1:-1]:
        # i 저순위 j 고순위
        indegree[i] += 1
        graph[j].append(i)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

# 꺼내진 값(now)는 고순위이다. 즉, 선수과목이다.
while q:
    now = q.popleft()
    
    for i in graph[now]:
        d[i] = max(d[i], d[now] + times[i])
        
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(d[1:])

# 해당 수강시간을 더했을 때 시간이 더 오래 걸리면 해당 강의에 대한 전체수강시간을 갱신한다.
