INF = int(1e9)

n = int(input())
graph = [None]
for i in range(n):
    graph.append([0] + list(map(int, input().split())))
    
d = [[INF] * (n+1) for _ in range(1 << n)]
d[1 << 0][1] = 0

for mask in range(1 << n):
    for cur in range(1, n+1):
        if d[mask][cur] == INF:
            continue
        
        for nxt in range(1, n+1):
            if mask & (1 << (nxt - 1)) or graph[cur][nxt] == 0:
                continue
            next_mask = mask | (1 << (nxt - 1))
            d[next_mask][nxt] = min(d[next_mask][nxt], d[mask][cur] + graph[cur][nxt])
    
final_mask = (1 << n) - 1
ans = INF
for cur in range(1, n+1):
    if graph[cur][1] != 0:
        ans = min(ans, d[final_mask][cur] + graph[cur][1])
        
print(ans)