# 구간DP
# sums[i][j] : i~j번 파일 총합
INF = int(1e9)

t = int(input())
for _ in range(t):
    n = int(input())
    files = [0] + list(map(int, input().split()))

    sums = [[0] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i == j:
                sums[i][j] = files[j]
            else:
                sums[i][j] = sums[i][j-1] + files[j]

    d = [[0] * (n+1) for _ in range(n+1)]
    for length in range(2, n+1):
        for st in range(1, n-length+2):
            en = st + length - 1
            d[st][en] = INF
            for k in range(st, en):
                d[st][en] = min(d[st][en], d[st][k] + d[k+1][en] + sums[st][en])

    print(d[1][n])