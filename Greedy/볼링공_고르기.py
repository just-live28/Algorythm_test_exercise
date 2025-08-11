n, m = map(int, input().split())
arr = list(map(int, input().split()))

data = [0] * 11
for i in arr:
    data[i] += 1

result = 0
for i in range(1, m+1):
    n -= data[i]
    result += data[i] * n

print(result)