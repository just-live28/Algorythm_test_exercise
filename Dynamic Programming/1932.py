n = int(input())
arr = [None]
for _ in range(n):
    arr.append(list(map(int, input().split())))

d = [[0] * n for _ in range(n+1)]
for i in range(n):
    d[n][i] = arr[n][i]

for i in range(n-1, 0, -1):
    for j in range(i):
        d[i][j] = max(d[i+1][j], d[i+1][j+1]) + arr[i][j]

print(d[1][0])