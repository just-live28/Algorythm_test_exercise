n = int(input())
arr = list(map(int, input().split()))
arr.reverse()
INF = int(1e9)

stack = [INF]
result = []
for height in arr:
    while height >= stack[-1]:
        stack.pop()
    if stack[-1] == INF:
        result.append(-1)
    else:
        result.append(stack[-1])
    stack.append(height)

result.reverse()
print(*result)