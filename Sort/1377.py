import sys
input = sys.stdin.readline

n = int(input())
arr = [0]
for _ in range(n):
    arr.append(int(input()))

sorted_arr = sorted(arr)
sorted_arr_idx = {}
for i in range(1, n+1):
    sorted_arr_idx[sorted_arr[i]] = i

max_diff = 0
for i in range(1, n+1):
    max_diff = max(max_diff, i - sorted_arr_idx[arr[i]])

print(max_diff + 1)