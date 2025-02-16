# n개 중 m개를 뽑는다

n, m = map(int, input().split())
arr = [x for x in range(1, n+1)]
result = [0] * n
visited = [-1] * (n+1)

# k개 수열이 들어있고, idx 상 k번째 수를 고르는 함수
def func(k):
    if k == m:
        print(*result[:m])
        return
    
    for i in range(1, n+1):
        if visited[i] == -1:
            visited[i] = 1
            result[k] = i
            func(k+1)
            visited[i] = -1

func(0)