from collections import deque

n = int(input())
arr = [0] * (n+1)
line = list(map(int, input().split()))
for i in range(1, n+1):
    arr[i] = line[i-1]

q = deque([x for x in range(1, n+1)])
result = []
while q:
    now = q.popleft()
    result.append(now)
    
    num = arr[now]
    if num > 0:
        q.rotate(-(num-1))
    else:
        q.rotate(-num)

print(*result)