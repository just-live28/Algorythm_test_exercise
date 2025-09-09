# 중복 X, 순열
# visited를 사용하고, 다음 것 선택에 1~n 반영

def func(k):
    if k == m:
        print(*arr[:m])
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            visited[i] = True
            arr[k] = i
            func(k+1)
            visited[i] = False

n, m = map(int, input().split())
arr = [0] * 10
visited = [False] * (n+1)
func(0)