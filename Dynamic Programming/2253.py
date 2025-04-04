INF = int(1e9)

n, m = map(int, input().split())
impossible = set()
for _ in range(m):
    impossible.add(int(input()))

d = [[INF] * 151 for _ in range(n+1)]
# n번째 돌에 k칸으로 점프했을 때 최소 횟수
d[1][0] = 0
if 2 not in impossible:
    d[2][1] = 1

for x in range(2, n):
    if x in impossible:
        continue
    for k in range(1, 151):
        for nk in (k-1, k, k+1):
            nx = x + nk
            if nx <= n and 1 <= nk <= 150 and nx not in impossible:
                d[nx][nk] = min(d[nx][nk], d[x][k] + 1)

result = min(d[n])
if result == INF:
    print(-1)
else:
    print(result)