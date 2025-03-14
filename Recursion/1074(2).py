# 0 1
# 2 3
# 0 <= a < 2 ** (n-1) | 2 ** (n-1) <= a < 2 ** n
# 0 <= b < 2 ** (n-1) | 2 ** (n-1) <= b < 2 ** n

def visit(n, a, b):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    if 0 <= a < half and 0 <= b < half:
        return visit(n-1, a, b)
    elif 0 <= a < half and half <= b < 2 ** n:
        return half * half + visit(n-1, a, b - half)
    elif 2 ** (n-1) <= a < 2 ** n and 0 <= b < 2 ** (n-1):
        return 2 * half * half + visit(n-1, a - half, b)
    else:
        return 3 * half * half + visit(n-1, a - half, b - half)

n, r, c = map(int, input().split())
print(visit(n, r, c))
    