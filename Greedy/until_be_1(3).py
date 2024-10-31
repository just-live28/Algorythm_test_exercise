n, k = map(int, input().split())

result = 0

while(n > 1):
    if n % k == 0:
        n //= k
        result += 1
    else:
        temp = n % k
        result += temp
        n -= temp

print(result)