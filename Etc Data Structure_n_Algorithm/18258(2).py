from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())
for _ in range(n):
    line = input().split()
    if len(line) == 2:
        q.append(line[1])
    elif line[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif line[0] == 'size':
        print(len(q))
    elif line[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    else:
        if not q:
            print(-1)
        else:
            print(q[-1])