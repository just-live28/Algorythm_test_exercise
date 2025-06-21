n = int(input())
arr = list(map(int, input().split()))

pivot = -1
for i in range(n-1, 0, -1):
    if arr[i-1] > arr[i]:
        pivot = i-1
        break

if pivot == -1:
    print(pivot)
else:
    max_num = 0
    max_idx = 0
    for j in range(n-1, pivot, -1):
        if arr[pivot] > arr[j] and arr[j] > max_num:
            max_num = arr[j]
            max_idx = j
    arr[pivot], arr[max_idx] = arr[max_idx], arr[pivot]

    remain = arr[pivot+1:]
    remain.sort(reverse=True)
    print(*(arr[:pivot+1] + remain))