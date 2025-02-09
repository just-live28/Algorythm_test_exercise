n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [-1] * n
result = [0] * n

def func(k):
    if k == m:
        print(*result[:m])
    
    for i in range(n):
        if visited[i] == -1:
            visited[i] = 1
            result[k] = arr[i]
            func(k+1)
            visited[i] = -1

func(0)