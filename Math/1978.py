n = int(input())
arr = list(map(int, input().split()))

def is_prime(number):
    if number == 1:
        return False
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
            break
        i += 1
    return True

count = 0
for num in arr:
    if is_prime(num):
        count += 1

print(count)