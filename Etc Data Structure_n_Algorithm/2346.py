from collections import deque

n = int(input())
arr = list(map(int, input().split()))
q = deque()
for i in range(1, n+1):
    q.append((i, arr[i-1]))

result = []
while q:
    idx, now = q.popleft()
    result.append(idx)

    if now > 0:
        q.rotate(-(now-1))
    else:
        q.rotate(-now)

print(*result)