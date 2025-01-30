from collections import deque

n, k = map(int, input().split())
dp = [int(1e9)] * 100001
dp[n] = 0

def append_queue(q, now, t):
    if 0 <= now+1 <= 100000:
        q.append((now+1, t+1))
    if 0 <= now-1 <= 100000:
        q.append((now-1, t+1))
    if 0 <= 2*now <= 100000:
        q.append((2*now, t))

q = deque()
append_queue(q, n, 0)

while q:
    now, t = q.popleft()
    if t < dp[now]:
        dp[now] = t
        append_queue(q, now, t)
        
print(dp[k])