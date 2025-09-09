# arr 주어짐 / 중복 X (visited 사용) / 오름차순 (조합, st 사용)

def func(k):
    if k == m:
        print(*result)
        return
    
    if k == 0:
        last = 0
    else:
        last = result[k-1]
    
    for i in range(n):
        if not visited[i] and arr[i] > last:
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