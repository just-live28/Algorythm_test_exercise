from collections import deque

n = int(input())
arr = list(map(int, input().split()))

q = deque(arr)
wait = []
cur = 1

while q:
    now = q.popleft()

    if now == cur:
        cur += 1

        while wait:
            top = wait.pop()
            if top == cur:
                cur += 1
            else:
                wait.append(top)
                break
    else:
        wait.append(now)

if cur == n+1:
    print('Nice')
else:
    print('Sad')