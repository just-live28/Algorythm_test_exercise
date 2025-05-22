dic = {}

n, k = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
sums = [0] * (n+1)
for i in range(1, n+1):
    sums[i] = sums[i-1] + arr[i-1]

    if sums[i] == k:
        result += 1

    prev = sums[i] - k
    if prev in dic:
        result += dic[prev]

    if sums[i] in dic:
        dic[sums[i]] += 1
    else:
        dic[sums[i]] = 1
    
print(result)