from collections import deque
import sys
input = sys.stdin.readline

q = deque()

n = int(input())

count = 0
for _ in range(n):
    line = list(input().split())
    
    if line[0] == 'push':
        count += 1
        q.append(int(line[1]))
    elif line[0] == 'pop':
        if count == 0:
            print(-1)
        else:
            count -= 1
            print(q.popleft())
    elif line[0] == 'size':
        print(count)
    elif line[0] == 'empty':
        if count == 0:
            print(1)
        else:
            print(0)
    elif line[0] == 'front':
        if count == 0:
            print(-1)
        else:
            print(q[0])
    elif line[0] == 'back':
        if count == 0:
            print(-1)
        else:
            print(q[-1])