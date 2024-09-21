n, k = map(int, input().split())

count = 0
while(True):
    if n < k:
        break
    
    if n % k != 0:
        target = n % k
        n -= target
        count += target
    else:
        n //= k
        count += 1

while n > 1:
    n -= 1
    count += 1

print(count)