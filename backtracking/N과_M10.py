# 수열 주어짐(정렬 필요, 같은수 존재) / 비내림차순 -> 중복 없는 조합

def func(k):
    if k == m:
        print(*result)
        return
    
    if k == 0:
        last = 0
    else:
        last = result[k-1]
    
    prev = 0
    for i in range(n):
        if not visited[i] and arr[i] >= last and arr[i] != prev:
            visited[i] = True
            result[k] = arr[i]
            prev = arr[i]
            func(k+1)
            visited[i] = False
    
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visited = [False] * n
result = [0] * m

func(0)