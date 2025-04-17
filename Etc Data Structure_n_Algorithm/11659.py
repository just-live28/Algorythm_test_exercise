import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sums = [0] * (n+1)
for a in range(1, n+1):
    sums[a] = sums[a-1] + arr[a]

for _ in range(m):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])