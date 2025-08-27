n = int(input())
arr = [None]
for _ in range(n):
    arr.append(int(input()))

d = [0] * 301
d[1] = arr[1]
if n > 1:
    d[2] = arr[1] + arr[2]

for i in range(3, n+1):
    d[i] = arr[i] + max(d[i-2], d[i-3] + arr[i-1])

print(d[n])