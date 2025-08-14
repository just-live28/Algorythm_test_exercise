INF = int(1e9)

n = int(input())
arr = list(map(int, input().split()))
stack = [0] * 4

def find_idx(num, stack):
    idx = 0
    min_diff = INF
    for i in range(4):
        diff = num - stack[i]
        if diff > 0:
            if diff < min_diff:
                min_diff = diff
                idx = i
    
    if min_diff == INF:
        return -1
    return idx

enable = True
for j in range(n):
    idx = find_idx(arr[j], stack)
    
    if idx == -1:
        enable = False
        break
    
    stack[idx] = arr[j]

if enable:
    print('YES')
else:
    print('NO')