from bisect import bisect_left

twos = []

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    for j in range(n):
        twos.append(arr[i] + arr[j])
twos.sort()

max_val = 0
for i in range(n):
    for j in range(n):
        idx = bisect_left(twos, arr[i] - arr[j])
        if idx < n:
            max_val = max(max_val, arr[idx])

print(max_val)