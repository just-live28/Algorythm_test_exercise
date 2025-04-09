# 조합

t = int(input())
for _ in range(t):
    n = int(input())

    d = [0] * (n+1)
    d[0] = 1
    for i in range(1, 4):
        for j in range(1, n+1):
            if j - i >= 0:
                d[j] += d[j-i]
                
    print(d[n])