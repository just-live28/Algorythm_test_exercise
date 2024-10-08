n = int(input())

arr = list(map(int, input().split()))
arr.reverse()

d = [1] * n

for i in range(1,n):
    for j in range(0, i):
        if arr[i] > arr[j]:
            d[i] = max(d[i], d[j]+1)

print(n-max(d))