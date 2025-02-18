n, m = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

result = []
idx1 = 0
idx2 = 0
for _ in range(n + m):
    if idx1 == n:
        result.append(arr2[idx2])
        idx2 += 1
    elif idx2 == m:
        result.append(arr1[idx1])
        idx1 += 1
    elif arr1[idx1] <= arr2[idx2]:
        result.append(arr1[idx1])
        idx1 += 1
    else:
        result.append(arr2[idx2])
        idx2 += 1

print(*result)