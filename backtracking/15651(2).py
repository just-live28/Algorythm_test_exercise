# 1~n 중 m개를 고른 수열
# 중복 가능

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
result = [0] * m

def func(k):
    if k == m:
        print(*result)
        return
    
    for i in range(n):
        result[k] = arr[i]
        func(k+1)

func(0)