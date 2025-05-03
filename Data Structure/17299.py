n = int(input())
arr = list(map(int, input().split()))

count = [0] * 1000001
count[0] = int(1e9)
for i in range(n):
    count[arr[i]] += 1

stk = []
stk.append(0)
result = [0] * n
for i in range(n-1, -1, -1):
    now = arr[i]
    now_count = count[now]
    
    while count[stk[-1]] <= now_count:
        stk.pop()
    
    if stk[-1] == 0:
        result[i] = -1
    else:
        result[i] = stk[-1]
    
    stk.append(now)
    
print(*result)