from collections import deque
import sys
input = sys.stdin.readline

eratos = [True] * 10001
eratos[0] = eratos[1] = False
for i in range(2, 101):
    if eratos[i]:
        for mul in range(i*i, 10001, i):
            eratos[mul] = False
            
n = int(input())
for _ in range(n):
    before, after = map(int, input().split())
    visited = [False] * 10001
    q = deque()
    q.append((0, before))
    result = int(1e9)
    while q:
        count, now = q.popleft()
        
        if now == after:
            result = count
            break
        
        for i in range(4):
            for j in range(10):
                nxt = now + j * (10 ** i) - (((now // (10 ** i)) % 10) * (10 ** i))
                if nxt > 999 and eratos[nxt] and not visited[nxt]:
                    visited[nxt] = True
                    q.append((count + 1, nxt))

    if result == int(1e9):
        print('Impossible')
    else:
        print(result)