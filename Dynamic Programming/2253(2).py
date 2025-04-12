INF = int(1e9)

n, m = map(int, input().split())
no_step = set()
for _ in range(m):
    no_step.add(int(input()))

d = [[INF] * 142 for _ in range(n+1)]
d[1][0] = 0
if 2 not in no_step:
    d[2][1] = 1

for x in range(2, n):
    if x in no_step:
        continue
    for k in range(1, 142):
        for nk in (k-1, k, k+1):
            nx = x + nk
            if 1 <= nk <= 141 and nx <= n and nx not in no_step:
                d[nx][nk] = min(d[nx][nk], d[x][k] + 1)

result = min(d[n])
if result == INF:
    print(-1)
else:
    print(result)