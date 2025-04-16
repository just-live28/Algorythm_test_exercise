import sys
sys.setrecursionlimit(10**5) 

def find_team(v):
    global count
    visited[v] = True
    next_v = matches[v]
    
    if not visited[next_v]:
        find_team(next_v)
    else:
        if not finished[next_v]:
            temp = next_v
            count_in_cycle = 1
            while temp != v:
                count_in_cycle += 1
                temp = matches[temp]
            count += count_in_cycle
    finished[v] = True

t = int(input())
for _ in range(t):
    n = int(input())
    matches = [0] + list(map(int, input().split()))
    
    visited = [False] * (n+1)
    finished = [False] * (n+1)
    count = 0
    
    for i in range(1, n+1):
        if not visited[i]:
            find_team(i)

    print(n - count)