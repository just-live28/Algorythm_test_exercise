n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

def count_router(arr, target_length):
    count = 1
    prev = arr[0]
    for i in range(1, n):
        if arr[i] - prev >= target_length:
            count += 1
            prev = arr[i]
    return count

start = 1
end = arr[-1] - arr[0]
max_length = 0
while start <= end:
    mid = (start + end) // 2
    
    router = count_router(arr, mid)
    if router >= c:
        max_length = mid
        start = mid + 1
    else:
        end = mid - 1

print(max_length)