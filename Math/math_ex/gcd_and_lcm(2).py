# gcd : 최대공약수
# (b%a, a) 로 계속 반복
# a가 0이 되면 b를 반환
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# lcm : 최소공배수
# a * b = gcd(a, b) * lcm(a, b)
def lcm(a, b):
    return a // gcd(a, b) * b 

print(gcd(12, 20))
print(lcm(12, 20))