# 1~n 까지 자연수 중 중복 없이 m 개를 고르기

# 중복 x, 순서 x, 고른 수열은 오름차순

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]

visited = [False] * n
result = [0] * m
def func(k, st):
    if k == m:
        print(*result)
        return
    
    for i in range(st, n):
        if not visited[i]:
            visited[i] = True
            result[k] = arr[i]
            func(k+1, i+1)
            visited[i] = False

func(0, 0)