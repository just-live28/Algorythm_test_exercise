import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 2 ~ 20
arr = [[] for _ in range(21)]
for i in range(n):
    name = input().rstrip()
    arr[len(name)].append(i)

result = 0
for group in arr[2:]:
    left = 0
    for right in range(len(group)):
        while group[right] - group[left] > k:
            left += 1
        result += right - left

print(result)