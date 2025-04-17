# 행렬 곱셈
# length: 2~n+1
# st: n - length + 2
# en:(반복문x) st + length - 1
INF = int(1e9)

n = int(input())
matrixes = [0]
for _ in range(n):
    r, c = map(int, input().split())
    matrixes.append((r, c))

d = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    d[i][i] = 0

for length in range(2, n+1):
    for st in range(1, n - length + 2):
        en = st + length - 1
        for k in range(st, en):
            d[st][en] = min(d[st][en], d[st][k] + d[k+1][en] + matrixes[st][0] * matrixes[k][1] * matrixes[en][1])

print(d[st][en])