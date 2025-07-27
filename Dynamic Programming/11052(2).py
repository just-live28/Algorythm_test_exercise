# 카드팩 N개, 각 카드팩 가격 Pi
# d[k]: k장일 때 최대지불액
# d[k] = max(d[k], d[k-i] + pi) (단, k-i >= 0)

n = int(input())
prices = [0] + list(map(int, input().split()))

d = [0] * (n+1)
for i in range(1, n+1):
    d[i] = prices[i]

for i in range(1, n+1):
    for j in range(1, i):
        d[i] = max(d[i], d[i-j] + prices[j])

print(d[n])