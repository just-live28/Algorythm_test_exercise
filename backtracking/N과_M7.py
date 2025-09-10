# 수열 주어짐(정렬 필요) / 중복 가능 / 순서 고려(순열)

def func(k):
    if k == m:
        print(*result)
        return

    for i in range(n):
        result[k] = arr[i]
        func(k+1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result = [0] * m

func(0)