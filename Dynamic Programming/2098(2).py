INF = int(1e9)

n = int(input())
MAX = 2 ** n - 1
w = [0]
for _ in range(n):
    w.append([0] + list(map(int, input().split())))

# d[stat][last_city]
d = [[INF] * (n+1) for _ in range(MAX+1)]
d[1][1] = 0
    
for stat in range(1 << n):
    for cur in range(1, n+1):
        if d[stat][cur] == INF:
            continue
        
        for nxt in range(1, n+1):
            if stat & (0 | 1 << (nxt-1)) == 0 and w[cur][nxt] != 0:
                nstat = stat | (1 << (nxt-1))
                d[nstat][nxt] = min(d[nstat][nxt], d[stat][cur] + w[cur][nxt])

answer = INF
for i in range(1, n+1):
    if w[i][1] != 0:
        answer = min(answer, d[MAX][i] + w[i][1])

print(answer)