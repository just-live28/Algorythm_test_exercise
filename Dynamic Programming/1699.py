n = int(input())

d = [0] + [x for x in range(1, n+1)]
for i in range(4, n+1):
    for j in range(1, int(i ** 0.5) + 1):
        d[i] = min(d[i], d[i- j**2] + 1)

print(d[n])