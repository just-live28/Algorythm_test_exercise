from collections import deque

n, k = map(int, input().split())
arr = ['?'] * n

cur = 0
crash = False
for _ in range(k):
    s, ch = input().split()

    cur = (cur + int(s)) % n

    if arr[cur] == '?':
        if ch in arr:
            crash = True
        else:
            arr[cur] = ch
    elif arr[cur] != ch:
        crash = True

if crash:
    print('!')
else:
    q = deque(arr)
    q.rotate(n-1 - cur)

    while q:
        print(q.pop(), end='')