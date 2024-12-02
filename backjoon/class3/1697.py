from collections import deque

n, k = map(int, input().split())

max_pos = 100000
visited = [False] * (max_pos+1)
visited[n] = True

q = deque()
q.append((n, 0))

while q:
    now, time = q.popleft()
    
    if now == k:
        print(time)
        break
    
    for next_pos in (now-1, now+1, now*2):
        if 0 <= next_pos <= max_pos and visited[next_pos] != True:
            visited[next_pos] = True
            q.append((next_pos, time+1))