INF = int(1e9)

n = int(input())
matrix = [None]
for _ in range(n):
    a, b = map(int, input().split())
    matrix.append((a, b))

if n == 1:
    print(0)
elif n == 2:
    print(matrix[1][0] * matrix[1][1] * matrix[2][1])
else:
    d = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j:
                d[i][j] = 0
    
    for length in range(2, n+1):
        for st in range(1, n-length+2):
            en = st+length-1
            for k in range(st, en):
                d[st][en] = min(d[st][en], d[st][k] + d[k+1][en] + matrix[st][0] * matrix[k][1] * matrix[en][1])

    print(d[1][n])