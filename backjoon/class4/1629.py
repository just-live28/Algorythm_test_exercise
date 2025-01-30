a, b, c = map(int, input().split())

def remain(a, n):
    if n == 1:
        return a % c
    else:
        half = remain(a, n//2)
        if n % 2 == 0:
            return (half * half) % c
        else:
            return (half * half * a) % c

print(remain(a, b))