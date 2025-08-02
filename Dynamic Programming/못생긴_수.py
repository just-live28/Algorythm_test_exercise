n = int(input())

arr = [1]
idx_2 = idx_3 = idx_5 = 0
for _ in range(n-1):
    num_2 = arr[idx_2] * 2
    num_3 = arr[idx_3] * 3
    num_5 = arr[idx_5] * 5

    min_num = min(num_2, num_3, num_5)
    arr.append(min_num)

    if min_num == num_2:
        idx_2 += 1
    if min_num == num_3:
        idx_3 += 1
    if min_num == num_5:
        idx_5 += 1

print(arr[-1])