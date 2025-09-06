import sys
sys.setrecursionlimit(10 ** 5)

def find_team(x):
    global result
    visited[x] = True
    
    nxt = arr[x]
    if not visited[nxt]:
        find_team(nxt)
    else:
        if not finished[nxt]:
            count = 1
            cur = nxt
            while cur != x:
                count += 1
                cur = arr[cur]
            result += count
    
    finished[x] = True
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [None] + list(map(int, input().split()))
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    result = 0
    for i in range(1, n+1):
        if not visited[i]:
            find_team(i)

    print(n - result)