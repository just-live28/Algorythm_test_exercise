n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]

result = [0] * m
visited = [False] * n

def func(k):
    if k == m:
        print(*result)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result[k] = arr[i]
            func(k+1)
            visited[i] = False

func(0)