# 수열 주어짐(정렬 필요, 같은 수 존재) / 순서 고려 / 중복 X

def func(k):
    if k == m:
        print(*result)
        return
    
    prev = 0
    for i in range(n):
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            result[k] = arr[i]
            prev = arr[i]
            func(k+1)
            visited[i] = False

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * m
visited = [False] * n

func(0)