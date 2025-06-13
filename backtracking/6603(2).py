def func(k):
    if k == 6:
        print(*result[:-1])
        return
    
    for i in range(n):
        if not visited[i] and arr[i] > result[k-1]:
            visited[i] = True
            result[k] = arr[i]
            func(k+1)
            visited[i] = False

# line이 0인 경우 종료
while True:
    line = list(map(int, input().split()))

    n = line[0]
    if n == 0:
        break
    arr = line[1:]

    result = [0] * 7
    visited = [False] * n
    func(0)
    print()