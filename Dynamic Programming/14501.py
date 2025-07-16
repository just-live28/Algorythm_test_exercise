n = int(input())
times = [0] * (n+2)
pays = [0] * (n+2)
for i in range(1, n+1):
    t, p = map(int, input().split())
    times[i] = t
    pays[i] = p

d = [0] * (n+2)
for i in range(n, 0, -1):
    if i + times[i] <= n+1:
        d[i] = max(pays[i] + d[i + times[i]], d[i+1])
    else:
        d[i] = d[i+1]

print(d[1])