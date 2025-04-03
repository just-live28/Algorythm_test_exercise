n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.reverse()

result = 0
for coin in coins:
    if k == 0:
        break
    
    quotient = k // coin
    if quotient > 0:
        result += quotient
        k -= quotient * coin
        
print(result)