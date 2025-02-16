n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = [0] * (n+1)
def func(k):
    if k == m:
        print(*result[:m])
        return
    
    prev = 0
    for i in arr:
        if prev != i and i >= result[k-1]:
            result[k] = i
            prev = i
            func(k+1)

func(0)