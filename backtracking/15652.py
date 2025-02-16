n, m = map(int, input().split())

arr = [0] * (n+1)

def func(k):
    if k == m:
        print(*arr[:m])
        return
    
    for i in range(1, n+1):
        if i >= arr[k-1]:
            arr[k] = i
            func(k+1)

func(0)