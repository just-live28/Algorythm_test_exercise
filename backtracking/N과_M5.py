# arr이 주어지고 / 중복 X(visited 사용) / 순열

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
    
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * n
result = [0] * m

func(0)