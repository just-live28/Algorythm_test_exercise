# 두 소수의 합

# 10000보다 작은 4 이상의 모든 짝수
# (차이, (n1, n2))
from itertools import combinations_with_replacement

numbers = [True] * 10001

for i in range(2, 101):
    if numbers[i]:
        cur = 2 * i
        while cur <= 10000:
            numbers[cur] = False
            cur += i

prime_numbers = []
for i in range(2, 10001):
    if numbers[i]:
        prime_numbers.append(i)

goldbach = {}
for a, b in combinations_with_replacement(prime_numbers, 2):
    if a + b in goldbach and b - a >= goldbach[a+b][0]:
        continue
    goldbach[a+b] = [b - a, (a, b)]

t = int(input())
for _ in range(t):
    print(*goldbach[int(input())][1])