p = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(11, 101):
    p.append(p[-1] + p[-5])

tc = int(input())

for _ in range(tc):
    n = int(input())
    print(p[n])