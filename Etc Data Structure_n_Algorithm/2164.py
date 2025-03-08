from collections import deque

n = int(input())
q = deque([x for x in range(1, n+1)])

if n == 1:
    print(q.popleft())
else:
    while True:
        q.popleft()
        if len(q) == 1:
            print(q.popleft())
            break
        q.append(q.popleft())