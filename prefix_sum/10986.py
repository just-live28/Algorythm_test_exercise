n, m = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0] * n
sums[0] = arr[0]
for i in range(1, n):
    sums[i] = sums[i-1] + arr[i]

result = 0
for length in range(1, n+1):
    for st in range(n-length+1):
        if length == 1:
            if arr[st] % 3 == 0:
                result += 1
            continue
        en = st + length - 1
        if st == 0:
            if sums[en] % 3 == 0:
                result += 1
        else:
            if (sums[en] - sums[st-1]) % 3 == 0:
                result += 1

print(result)