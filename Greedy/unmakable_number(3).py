n = int(input())
coins = list(map(int, input().split()))
coins.sort()

total = 1
for coin in coins:
    if total >= coin:
        total += coin

print(total)