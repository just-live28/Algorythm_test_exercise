import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(map(int, input().split()))

sums = [0] * (n+1)
sums[0] = arr[0]
for i in range(1, n):
    sums[i] = sums[i-1] + arr[i]

for _ in range(m):
    i, j = map(int, input().split())
    print(sums[j-1] - sums[i-2])