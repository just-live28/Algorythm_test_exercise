# a를 b번 곱한 수를 c로 나눈 나머지

# a * b % m = (a * (2/b) % m) * (a * (2/b) % m) % m

def func(a, b ,c):
    if b == 1:
        return a % c
    
    half = func(a, b//2, c)
    if b % 2 == 0:
        return (half * half) % c
    else:
        return ((a % c) * half * half) % c

a, b, c = map(int, input().split())
print(func(a, b, c))