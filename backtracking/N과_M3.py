# 중복 허용(visited 미사용), 순열

def func(k):
    if k == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        arr[k] = i
        func(k+1)

n, m = map(int, input().split())
arr = [0] * m
func(0)