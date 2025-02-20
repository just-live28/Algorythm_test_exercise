def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def cal_kaing_number(m, n, x, y):
    max_limit = lcm(m, n)
    k = x
    while k <= max_limit:
        if (k - 1) % n + 1 == y:
            return k
        k += m
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(cal_kaing_number(m, n, x, y))