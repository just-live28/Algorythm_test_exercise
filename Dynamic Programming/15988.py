t = int(input())
for _ in range(t):
    n = int(input())

    d = [0] * 1000001
    d[1], d[2], d[3] = 1, 2, 4

    if n <= 3:
        print(d[n])
        continue

    for i in range(4, n+1):
        d[i] = (d[i-1] + d[i-2] + d[i-3]) % 1000000009

    print(d[n])