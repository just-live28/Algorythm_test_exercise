t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    d = [0] * 10001
    d[0] = 1
    # coins 순회문을 안에 두면 순열, 바깥에 두면 조합
    for coin in coins:
        for i in range(coin, m+1):
            d[i] += d[i-coin]
    print(d[m])