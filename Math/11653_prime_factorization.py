n = int(input())

if n != 1:
    i = 2
    while n != 1:
        if i * i > n:
            break
        if n % i == 0:
            while n % i == 0:
                n //= i
                print(i)
        i += 1
    
    if n != 1:
        print(n)