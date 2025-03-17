n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
result = [0] * m

def func(k, st):
    if k == m:
        print(*result)
        return
    
    for i in range(st, n):
        result[k] = arr[i]
        func(k+1, i)

func(0, 0)