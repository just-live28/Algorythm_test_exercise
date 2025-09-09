# 중복 X(visited 사용), 오름차순(조합, arr[k-1]보다 i가 커야 함, k가 0인 경우 arr배열을 m보다 크게 만들어 무조건 0이 나오도록 설계)

def func(k):
    if k == m:
        print(*arr)
        return
    
    if k == 0:
        st = 1
    else:
        st = arr[k-1] + 1
        
    for i in range(st, n+1):
        if not visited[i]:
            visited[i] = True
            arr[k] = i
            func(k+1)
            visited[i] = False
    
n, m = map(int, input().split())
arr = [0] * m
visited = [False] * (n+1)
func(0)