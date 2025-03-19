n = int(input())

def divisor(n):
    arr = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            arr.append(i)
            if i * i != n:
                arr.append(n // i)
        i += 1
    return sorted(arr)

print(divisor(n))