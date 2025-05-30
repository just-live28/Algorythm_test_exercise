from collections import deque
INF = int(1e9)

n, k = map(int, input().split())

q = deque()
q.append((0, n))
visited = [INF] * 100001

while q:
    time, now = q.popleft()

    if now == k:
        visited[k] = min(visited[k], time)
    
    if time < visited[now]:
        visited[now] = time

        if 0 <= now-1 <= 100000:
            q.append((time+1, now-1))
        if 0 <= now+1 <= 100000:
            q.append((time+1, now+1))
        if 0 <= now * 2 <= 100000:
            q.append((time, now * 2))

print(visited[k])
