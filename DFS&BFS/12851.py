from collections import deque
INF = int(1e9)

n, k = map(int, input().split())

visited = [INF] * 100001
visited[n] = 0
q = deque()
q.append((0, n))

min_time = int(1e9)
count = 0
while q:
    time, now = q.popleft()
    
    if now == k:
        if time < min_time:
            min_time = time
            count = 1
        elif time == min_time:
            count += 1
        continue

    for nxt in [now-1, now+1, now*2]:
        if 0 <= nxt <= 100000 and time+1 <= visited[nxt]:
            visited[nxt] = time+1
            q.append((time+1, nxt))

print(min_time)
print(count)