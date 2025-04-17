import sys
sys.setrecursionlimit(10**5)

def find_team(x):
    global COUNT
    visited[x] = True
    next_x = arr[x]
    
    if not visited[next_x]:
        find_team(next_x)
    else:
        if not finished[next_x]:
            cur = next_x
            cycle_count = 1
            while (cur != x):
                cycle_count += 1
                cur = arr[cur]
            COUNT += cycle_count
    finished[x] = True
    
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    COUNT = 0

    for i in range(1, n+1):
        if not visited[i]:
            find_team(i)

    print(n - COUNT)