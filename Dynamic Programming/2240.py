t, w = map(int, input().split())
arr = [None]
for _ in range(t):
    num = int(input())
    arr.append(num)

d = [[[0] * 3 for _ in range(w+1)] for _ in range(t+1)]
move = 0
for i in range(1, t+1):
    # 안 움직였을 때 (초깃값)
    d[i][0][1] = d[i-1][0][1]
    if arr[i] == 1:
        d[i][0][1] += 1
    
    for j in range(1, w+1):
        if j > i:
            break
        
        if arr[i] == 1:
            d[i][j][1] = max(d[i-1][j-1][2], d[i-1][j][1]) + 1
            d[i][j][2] = max(d[i-1][j-1][1], d[i-1][j][2])
        else:
            d[i][j][1] = max(d[i-1][j-1][2], d[i-1][j][1])
            d[i][j][2] = max(d[i-1][j-1][1], d[i-1][j][2]) + 1
    
result = 0
for i in range(w+1):
    result = max(result, d[t][i][1], d[t][i][2])

print(result)