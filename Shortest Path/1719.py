INF = int(1e9)

n, m = map(int, input().split())

distance = [[INF] * (n+1) for _ in range(n+1)]
result = [[-1] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            result[i][i] = '-'
            distance[i][i] = 0
        else:
            result[i][j] = j

for _ in range(m):
    a, b, c = map(int, input().split())

    distance[a][b] = c
    distance[b][a] = c

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist = distance[i][k] + distance[k][j]

            if dist < distance[i][j]:
                first = k
                while True:
                    if result[i][first] == first:
                        break
                    first = result[i][first]
                result[i][j] = first
                distance[i][j] = dist

for i in range(1, n+1):
    print(*result[i][1:])