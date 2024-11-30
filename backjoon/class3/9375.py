tc = int(input())

for _ in range(tc):
    n = int(input())

    ootd = {}

    for _ in range(n):
        _, b = input().split()
        ootd[b] = ootd.get(b, 0) + 1

    result = 1
    for i in ootd.values():
        result *= i + 1

    print(result - 1)