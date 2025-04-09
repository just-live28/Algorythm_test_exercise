# 카드가 적더라도 가격이 비싸면 좋은 카드가 많이 있을 것이다

# 카드 i개 팩 가격은 Pi
# max가 최적해

# 조합 

n = int(input())
cards = list(map(int, input().split()))

d = [0] * (n+1)
for i in range(1, n+1):
    d[i] = cards[i-1]

for i in range(1, n+1):
    for j in range(1, n+1):
        if j - i >= 0:
            d[j] = max(d[j], d[j-i] + cards[i-1])

print(d[n])