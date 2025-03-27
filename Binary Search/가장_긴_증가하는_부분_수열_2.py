from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(n):
    idx = bisect_left(result, arr[i])
    if idx == len(result):
        result.append(arr[i])
    else:
        result[idx] = arr[i]

print(len(result))