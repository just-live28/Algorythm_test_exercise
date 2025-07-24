INF = int(1e9)

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def kadane(cols):
    max_sum = -INF
    cur_sum = 0

    for num in cols:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    
    return max_sum

result = -INF
for x2 in range(n):
    for x1 in range(x2+1):
        if x1 == x2:
            arr = board[x1]
        else:
            arr = []
            for i in range(m):
                node = 0
                for j in range(x1, x2+1):
                    node += board[j][i]
                arr.append(node)
        
        result = max(result, kadane(arr))

print(result)