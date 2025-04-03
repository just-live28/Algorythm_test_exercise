INF = int(1e9)

n, m = map(int, input().split())
impossible = set()
for _ in range(m):
    impossible.add(int(input()))

d = [[INF] * (n+1) for _ in range(150)]
# n번째 돌에 k칸으로 점프했을 때 최소 횟수
d[0][1] = 0
if 2 not in impossible:
    d[1][2] = 1

for x in range(2, n):
    for k in range(150):
        for nk in [k-1, k, k+1]:
            nx = x + nk
            if nx <= n and 1 <= nk <= 150 and nx not in impossible:
                d[nk][nx] = min(d[nk][nx], d[k][x] + 1)

result = min(d[i][-1] for i in range(150))
if result == INF:
    print(-1)
else:
    print(result)