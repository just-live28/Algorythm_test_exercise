n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

d = [1] * n
for i in range(1, n):
    for j in range(i):
        if (arr[j][0] < arr[i][0] and arr[j][1] < arr[i][1]) or (arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]):
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))