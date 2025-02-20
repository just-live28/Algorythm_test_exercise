# 가장 큰 동전부터 가능한 만큼 써서 액수를 줄인다.
# 동전이 안들어가면 동전 크기를 줄이면서 액수가 0이 될 때까지 반복한다.

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    
    if k >= coins[i]:
        count += k // coins[i]
        k %= coins[i]

print(count)