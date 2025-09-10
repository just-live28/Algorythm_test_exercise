# 수열 주어짐(정렬 필요, 같은 수 존재) / 중복 가능 / 순서 고려

def func(k):
    if k == m:
        print(*result)
        return
    
    prev = 0
    for i in range(n):
        if arr[i] != prev:
            result[k] = arr[i]
            prev = arr[i]
            func(k+1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * m

func(0)