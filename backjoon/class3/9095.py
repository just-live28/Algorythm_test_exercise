d = [0] * 11
d[1], d[2], d[3] = 1, 2, 4

for i in range(4, 11):
    d[i] = d[i-3] + d[i-2] + d[i-1]

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(d[n])