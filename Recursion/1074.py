def cal_z(n, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n-1)
    if 2 ** (n-1) <= r < 2 ** n:
        if 2 ** (n-1) <= c < 2 ** n:
            return half * half * 3 + cal_z(n-1, r - half, c - half)
        else:
            return half * half * 2 + cal_z(n-1, r - half, c)
    else:
        if 2 ** (n-1) <= c < 2 ** n:
            return half * half + cal_z(n-1, r, c - half)
        else:
            return cal_z(n-1, r, c)

n, r, c = map(int, input().split())
print(cal_z(n, r, c))