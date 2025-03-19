n = int(input())

def prime_factorization(n):
    if n == 1:
        return
    
    i = 2
    while n > 1:
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            print(i)
        i += 1
            
prime_factorization(n)