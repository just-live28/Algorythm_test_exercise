def func(n, r, c):
    if n == 1:
        return 0
    
    half = n // 2
    if 0 <= r < half and 0 <= c < half:
        return func(half, r, c)
    elif 0 <= r < half and half <= c < n:
        return half * half + func(half, r, c - half)
    elif half <= r < n and 0 <= c < half:
        return 2 * half * half + func(half, r - half, c)
    elif half <= r < n and half <= c < n:
        return 3 * half * half + func(half, r - half, c - half)

N, r, c= map(int, input().split())
print(func(2 ** N, r, c))