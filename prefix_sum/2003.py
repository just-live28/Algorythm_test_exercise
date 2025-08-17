n, m = map(int, input().split())
arr = list(map(int, input().split()))

sums = [0] * (n+1)
sums[0] = 0
for i in range(1, n+1):
    sums[i] = sums[i-1] + arr[i-1]
    
# i~j의 합: sums[j] - sums[i-1]
lp = rp = 0
result = 0
while rp <= n:
    total_sum = sums[rp] - sums[lp]
    
    if total_sum <= m:
        if total_sum == m:
            result += 1
        rp += 1
    else:
        lp += 1

print(result)