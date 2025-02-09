n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [-1] * n
result = [0] * (n+1)

def func(k):
    if k == m:
        print(*result[:m])
        return
    
    prev = 0
    for i in range(n):
        if visited[i] == -1 and prev != arr[i] and arr[i] >= result[k-1]:
            visited[i] = 1
            prev = arr[i]
            result[k] = arr[i]
            func(k+1)
            visited[i] = -1

func(0)