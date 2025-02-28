from collections import deque
# a b 이렇게 받으면 a -> b라는 뜻.
# 이러면 a가 고순위, b가 저순위
# 저순위의 indegree 증가한다.
# graph[고순위].append(저순위)

n = int(input())
indegree = [0] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(result)