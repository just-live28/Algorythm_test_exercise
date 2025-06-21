n = int(input())
arr = list(map(int, input().split()))

d = [x for x in arr]

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            d[i] = max(d[i], d[j] + arr[i])

print(max(d))