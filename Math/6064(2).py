def gcd(a, b):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a, b):
    return a // gcd(a,b) * b

def kaing(m, n, x, y):
    if x == m:
        x = 0
    if y == n:
        y = 0
    
    max_limit = lcm(m, n)
    i = x
    while i <= max_limit:
        if i != 0 and i % n == y:
                return i
        i += m
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(kaing(m, n, x, y))