n = int(input())

d = [0] + [x for x in range(1, n+1)]
for i in range(1, n+1):
    j = 1
    while j * j <= i:
        d[i] = min(d[i], d[i - j * j] + 1)
        j += 1

print(d[n])