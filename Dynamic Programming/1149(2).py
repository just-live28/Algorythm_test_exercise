n = int(input())
costs = [0]
for _ in range(n):
    r, g, b = map(int, input().split())
    costs.append((r, g, b))

d = [[0] * 3 for _ in range(n+1)]
for i in range(1, n+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + costs[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + costs[i][1]
    d[i][2] = min(d[i-1][0], d[i-1][1]) + costs[i][2]

print(min(d[n]))