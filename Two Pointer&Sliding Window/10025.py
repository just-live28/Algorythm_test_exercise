n, k = map(int, input().split())
arr = [0] * 1000001
max_x = 0
for _ in range(n):
    g, x = map(int, input().split())
    max_x = max(max_x, x)
    arr[x] = g
    
sums = [0] * (max_x + 1)
sums[0] = arr[0]
for i in range(1, max_x + 1):
    sums[i] = sums[i-1] + arr[i]

max_sum = 0
for i in range(max_x + 1):
    st = max(0, i-k)
    en = min(max_x, i+k)
    
    if st == 0:
        val = sums[en]
    else:
        val = sums[en] - sums[st-1]

    max_sum = max(max_sum, val)

print(max_sum)