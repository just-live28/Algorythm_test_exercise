# a가 b보다 클 때

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# print(gcd(120, 18)) -> 6

def lcm(a, b):
    return a // gcd(a, b) * b

print(lcm(120,18))