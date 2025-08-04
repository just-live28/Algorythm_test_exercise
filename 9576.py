# n 책 수 (1~N번) / m 사람 수
# 사람마다 a <= num <= b 의 책을 줄 수 있음

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for _ in range(m):
        a, b = map(int, input().split())
        arr.append((a, b))
    arr.sort(key = lambda x : x[1])

    visited = [False] * (n+1)
    result = 0
    for st, en in arr:
        for book in range(st, en+1):
            if not visited[book]:
                visited[book] = True
                result += 1
                break
                
    print(result)