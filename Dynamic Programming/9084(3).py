# 1차원 DP 풀이
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     coins = list(map(int, input().split()))
#     m = int(input())

#     d = [0] * (m+1)
#     d[0] = 1
#     for coin in coins:
#         for i in range(1, m+1):
#             if i - coin >= 0:
#                 d[i] += d[i-coin]

#     print(d[m])

# 2차원 dp 풀이
t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    d = [[0] * (m+1) for _ in range(n)]
    for i in range(n):
        d[i][0] = 1

    for i in range(n):
        for j in range(1, m+1):
            if i-1 >= 0:
                d[i][j] += d[i-1][j]
            
            if j - coins[i] >= 0:
                d[i][j] += d[i][j - coins[i]]

    print(d[n-1][m])