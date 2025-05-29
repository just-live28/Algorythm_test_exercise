import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def count_machine(arr, length):
    count = 1
    prev = arr[0]
    for h in range(1, n):
        if arr[h] - prev >= length:
            count += 1
            prev = arr[h]
    return count

min_range = 1
max_range = arr[-1] - arr[0]

result = 0
while (min_range <= max_range):
    mid = (min_range + max_range) // 2

    count = count_machine(arr, mid)

    if count >= c:
        result = mid
        min_range = mid + 1
    else:
        max_range = mid - 1

print(result)