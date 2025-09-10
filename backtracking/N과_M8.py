# 수열 주어짐(정렬 필요) / 중복 가능 / 비내림차순 -> 중복 가능한 조합

def func(k):
    if k == m:
        print(*result)
        return
    
    if k == 0:
        last = 0
    else:
        last = result[k-1]
    
    for i in range(n):
        if arr[i] >= last:
            result[k] = arr[i]
            func(k+1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * m

func(0)