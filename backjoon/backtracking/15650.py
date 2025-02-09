n, m = map(int, input().split())

arr = [0] * (n+1)
visited = [-1] * n

def func(k):
    if k == m:
        print(*arr[:m])
    
    for i in range(n):
        if visited[i] == -1 and i+1 > arr[k-1]:
            arr[k] = i+1
            visited[i] = 1
            func(k+1)
            visited[i] = -1

func(0)