n = int(input())
coins = list(map(int, input().split()))
coins.sort()

cur = 1
for coin in coins:
    if coin <= cur:
        cur += coin
    else:
        break

print(cur)