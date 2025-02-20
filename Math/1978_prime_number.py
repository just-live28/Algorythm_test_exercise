# 2부터 n-1까지
n = int(input())
arr = list(map(int, input().split()))

count = 0
for number in arr:
    if number == 1:
        continue
    is_prime = True
    i = 2
    while (i * i <= number):
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        count += 1

print(count)