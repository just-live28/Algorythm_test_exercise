n = int(input())
arr = [0] + list(map(int, input().split()))

if n == 1:
    print(arr[1])
else:
    d = [[0] * 2 for _ in range(n+1)]
    d[0][0] = d[0][1] = -int(1e9)

    result = -int(1e9)
    for i in range(1, n+1):
        d[i][0] = max(d[i-1][0] + arr[i], arr[i])
        d[i][1] = max(d[i-1][1] + arr[i], d[i-1][0])
        result = max(result, d[i][0], d[i][1])

    print(result)