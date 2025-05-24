n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

idx_table = [n-1] * n
count = 0
while count < n:
    
    max_num = arr[idx_table[0]][0]
    max_idx = 0
    for i in range(1, n):
        if arr[idx_table[i]][i] > max_num:
            max_num = arr[idx_table[i]][i]
            max_idx = i

    idx_table[max_idx] -= 1
    count += 1

    if count == n:
        print(max_num)
        break