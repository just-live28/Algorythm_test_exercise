import sys
input = sys.stdin.readline
NOT_VISITED = 0
IS_CYCLE = -1

def find_team(x):
    cur = x
    while True:
        visited[cur] = x
        cur = arr[cur]
        
        # 이번에 방문했던 학생을 만나는 경우(사이클 발생)
        if visited[cur] == x:
            while visited[cur] != IS_CYCLE:
                visited[cur] = IS_CYCLE
                cur = arr[cur]
            return
        # 이전에 방문했던 학생을 만나는 경우
        elif visited[cur] != NOT_VISITED:
            return

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [None] + list(map(int, input().split()))
    visited = [0] * (n+1)
    for i in range(1, n+1):
        if visited[i] == NOT_VISITED:
            find_team(i)

    count = 0
    for i in range(1, n+1):
        if visited[i] != IS_CYCLE:
            count += 1
    print(count)