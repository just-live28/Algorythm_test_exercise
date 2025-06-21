# floyd-washall로, 특정 학생에 대해 다른 모든 학생에게 도달할 수 있으면 정확한 순위를 알 수 있는 학생
# i->j 가 도달 가능하거나, j->i가 도달 가능하면 순위를 알 수 있는 것. 이를 본인을 제외하고 다 알 수 있어야 정확한 순위를 알 수 있음.
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

d = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    d[a][b] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])

result = 0
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if i == j:
            continue
        elif d[i][j] != INF or d[j][i] != INF:
            count += 1
    
    if count == n-1:
        result += 1

print(result)