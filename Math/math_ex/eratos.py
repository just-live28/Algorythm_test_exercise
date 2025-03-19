# 1~n 범위의 소수 목록 구하기
n = int(input())

def eratos(n):
    state = [True] * (n+1)
    if n == 1:
        return None

    i = 2   
    while i * i <= n:
        if not state[i]:
            i += 1
            continue
        j = i * i
        while j <= n:
            state[j] = False
            j += i
        i += 1

    primes = []
    for i in range(2, n+1):
        if state[i]:
            primes.append(i)
    return primes
