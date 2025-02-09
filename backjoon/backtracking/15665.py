n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

result = [0] * n
def func(k):
    if k == m:
        print(*result[:m])
        return
    
    prev = 0
    for i in arr:
        if prev != i:
             result[k] = i
             prev = i
             func(k+1)

func(0)