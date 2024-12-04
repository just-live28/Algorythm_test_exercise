import math

INF = int(1e9)
d = [4] * 50001

MAX_SQRT = math.trunc(math.sqrt(50000))

for i in range(1, MAX_SQRT + 1):
    d[i**2] = 1

n = int(input())

for i in range(1, n + 1):
    for j in range(math.trunc(math.sqrt(i)), 0, -1):
        d[i] = min(d[i], d[i - j**2] + 1)

print(d[n])