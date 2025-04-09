# 순열

t = int(input())
for _ in range(t):
    n = int(input())

    d = [0] * (n+1)
    d[0] = 1
    for i in range(1, n+1):
        for num in range(1, 4):
            if i - num >= 0:
                d[i] += d[i-num]

    print(d[n])