# a**b % m
# each = b // 2
# (a**each % m ) * (a**each % m ) * (a % m)

# b == 1:
# return a % m
a, b, c = map(int, input().split())

def func(a, b, m):
    if b == 1:
        return a % m
    
    half = func(a, b // 2, m)
    if b % 2 == 0:
        return (half * half) % m
    else:
        return (half * half * (a % m)) % m
    
print(func(a, b, c))