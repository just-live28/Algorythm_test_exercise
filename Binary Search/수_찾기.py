from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
finds = list(map(int, input().split()))

for find in finds:
    idx = bisect_left(arr, find)
    if idx == n or (idx == 0 and find != arr[0]):
        print(0)
    else:
        print(1)