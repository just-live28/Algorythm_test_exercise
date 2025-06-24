import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

result = 0
cur = 1
for i in arr:
    result += abs(cur - i)
    cur += 1

print(result)