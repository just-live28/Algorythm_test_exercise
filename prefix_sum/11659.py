import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sums = [0] * (n+1)
sums[1] = arr[1]
for i in range(2, n+1):
    sums[i] = sums[i-1] + arr[i]

for _ in range(m):
    a, b = map(int, input().split())
    print(sums[b] - sums[a-1])