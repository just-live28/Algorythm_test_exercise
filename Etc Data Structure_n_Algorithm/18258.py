from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())
for _ in range(n):
    cmd = input().split()
    if len(cmd) == 2:
        q.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif cmd[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])