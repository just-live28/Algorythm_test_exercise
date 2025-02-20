# 에라토스테네스의 채
m, n = map(int, input().split())

prime_numbers = [True] * 1000001
prime_numbers[1] = False

for i in range(2, n+1):
    if i * i > n:
        break
    if not prime_numbers[i]:
        continue
    j = i * i
    while j <= n:
        prime_numbers[j] = False
        j += i

for k in range(m, n+1):
    if prime_numbers[k]:
        print(k)