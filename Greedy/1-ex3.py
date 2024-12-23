n, k = map(int, input().split())

count = 0
while n > k:
    if n % k == 0:
        count += 1
        n //= k
    else:
        target = n % k
        count += target
        n -= target

print(count + (n-1))