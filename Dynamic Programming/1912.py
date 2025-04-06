n = int(input())
arr = list(map(int, input().split()))
INF = int(1e9)

sums = [0] * (n+1)
sums[1] = arr[0]
for i in range(2, n+1):
    sums[i] = sums[i-1] + arr[i-1]
print(sums[1:])



# d[st][en]
if n == 1:
    print(arr[0])
elif n == 2:
    print(max(arr[0], arr[1], sums[2]))    
else:
    d = [[0] * (n+1) for _ in range(n+1)]
    
    for length in range(2, n+1):
        for st in range(1, n - length + 2):
            en = st + length - 1
            d[st][en] = -INF
            for k in range(st, en):
                d[st][en] = max(d[st][en], sums[k], sums[en] - sums[k-1])

print(d[st][en])