import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

result = 0
for i in range(n):
    if (i + 1) % 3 == 0:
        continue
    result += arr[i]

print(result)