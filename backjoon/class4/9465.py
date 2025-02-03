tc = int(input())
for _ in range(tc):
    n = int(input())

    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    
    if n == 1:
        print(max(arr[0][0], arr[1][0]))
        continue
    elif n == 2:
        print(max(arr[1][0] + arr[0][1], arr[0][0] + arr[1][1]))
        continue

    d = [[0] * n for _ in range(2)]

    d[0][0] = arr[0][0]
    d[1][0] = arr[1][0]
    d[0][1] = arr[1][0] + arr[0][1]
    d[1][1] = arr[0][0] + arr[1][1]

    for i in range(2, n):
        d[0][i] = max(d[1][i-1] + arr[0][i], d[1][i-2] + arr[0][i])
        d[1][i] = max(d[0][i-1] + arr[1][i], d[0][i-2] + arr[1][i])

    print(max(d[0][n-1], d[1][n-1]))