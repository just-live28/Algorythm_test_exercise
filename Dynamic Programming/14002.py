n = int(input())
arr = list(map(int, input().split()))

d = [1] * (n+1)
route = [[] for _ in range(n+1)]

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            if d[i] < d[j] + 1:
                d[i] = d[j] + 1
                route[i] = [j]

idx = d.index(max(d))
result = []
while route[idx]:
    result.append(arr[idx])
    idx = route[idx][0]
result.append(arr[idx])
result.reverse()
print(max(d))
print(*result)