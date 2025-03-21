# a ** b % c

def func(a, b, c):
    if b == 0:
        return 1
    
    half = func(a, b // 2, c)
    
    if b % 2 == 1:
        return a * half * half % c
    else:
        return half * half % c

a, b, c = map(int, input().split())
print(func(a, b, c))