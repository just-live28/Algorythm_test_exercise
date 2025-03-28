n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(arr[i] + d[i-2], d[i-1])

print(d[n-1])