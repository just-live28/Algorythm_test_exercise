# n 승수 rc 행렬
n, r, c = map(int, input().split())

result = 0
while n > 0:
    if 0 <= r < 2**n // 2 and 0 <= c < 2**n // 2:
        result += 0
    elif 0 <= r < 2**n // 2 and 2**n // 2 <= c < 2**n:
        result += 1 * 2**(2 * n - 2)
        c -= 2**(n-1)
    elif 2**n // 2 <= r < 2**n and 0 <= c < 2**n // 2:
        result += 2 * 2**(2 * n - 2)
        r -= 2**(n-1)
    elif 2**n // 2 <= r < 2**n and 2**n // 2 <= c < 2**n:
        result += 3 * 2**(2 * n - 2)
        r -= 2**(n-1)
        c -= 2**(n-1)
    n -= 1

print(result)