d = [0] * 12
d[1] = 1
d[2] = d[1] + 1
d[3] = d[1] + d[2] + 1
for i in range(4, 12):
    d[i] = d[i-3] + d[i-2] + d[i-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n])