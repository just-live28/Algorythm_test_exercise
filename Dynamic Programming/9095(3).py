import sys
input = sys.stdin.readline
# d[n]: n을 1,2,3의 합으로 나타내는 방법의 수
# d[i] = d[i-3] + d[i-2] + d[i-1] (단, i > 3)

t = int(input())
for _ in range(t):
    n = int(input())

    d = [0] * 11
    d[1], d[2], d[3] = 1, 2, 4

    if n <= 3:
        print(d[n])
    else:
        for i in range(4, n+1):
            d[i] = d[i-3] + d[i-2] + d[i-1]
        print(d[n])