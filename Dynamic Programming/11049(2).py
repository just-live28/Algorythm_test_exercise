INF = int(1e9)

n = int(input())

arr = [0]
for _ in range(n):
    r, c = map(int, input().split())
    arr.append((r, c))

# 행렬 곱셈: r1 * c1(or r2) * c2

if n == 1:
    print(0)
elif n == 2:
    print(arr[1][0] * arr[1][1] * arr[2][1])
else:
    d = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        d[i][i] = 0

    for length in range(2, n+1):
        for st in range(1, n-length+2):
            en = st + length - 1
            for k in range(st, en):
                d[st][en] = min(d[st][en], d[st][k] + d[k+1][en] + arr[st][0] * arr[k][1] * arr[en][1])

    print(d[st][en])