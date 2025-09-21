def inf_func(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    
    memo[n] = inf_func(n // p, memo) + inf_func(n // q, memo)
    return memo[n]

n, p, q = map(int, input().split())
memo = {}

print(inf_func(n, memo))